from django.shortcuts import render ,redirect
from rest_framework.decorators import api_view 
from .utils import randomString 
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required ,permission_required
from .permissions import perff
from django.contrib.auth import authenticate ,login,logout
from .models import CustomUser ,OTP ,RESERVATIONS
from .forms import signupdata_form , logindata_form ,passwordotp_form ,passwordreset_form ,reservedata_form
# import 

@api_view(["GET"])
def index (req):
  if(req.user):
    print(req.user)
  return   render(req,"home.html")

@api_view(["GET"])
def aboutus (req):
  return   render(req,"aboutus.html")

@api_view(["GET"])
@login_required(login_url="/login")
def reservations (req):
  
  res = RESERVATIONS.objects.filter(email=req.user.email)
  return   render(req,"reservations.html",{res :res})



@api_view(["GET"])
def contactus (req):
  return   render(req,"contactus.html")

@api_view(["GET","POST"])
@login_required(login_url="/login")
def book (req):
  if(req.method=="POST"):
    data = reservedata_form(req.data)
    if(data.is_valid()):
        id = randomString(12)
        RESERVATIONS.objects.create(req.data,id=id)
        messages.info(req, f"""resevrtions booked  
                      reservation id {id}
                      """)

    
        return   render(req,"message.html",success="/")
    messages.info(req, f"""
  error in booking reservations
                      """)
    return   render(req,"bookreservation.html")
      
      
  else:
    print(req.user)
    return   render(req,"bookreservation.html")




@api_view(["GET"])
@login_required(login_url="/login")
# @permission_required("user")
def deleteres (req):
  RESERVATIONS.objects.delete(id=req.params.id)

  return   render(req,"reservations.html")

# @api_view(["POST"])
# @login_required(login_url="/login")
# # @permission_required("user")
# def bookreserve (req):
  







@api_view(["POST","GET"])
def login(req):
    print(req.method,"Sss")
    if req.method=="POST":
  
   
      dataser = logindata_form(req.POST)
      print(req.POST,dataser.is_valid(),req.POST["email"])
      if(dataser.is_valid()):  

      
      
        user_ = authenticate(req,email =req.POST["email"],password=req.POST["password"])
        print(user_,"Sdsd")
  
      
        if (user_ is not None):
          
                  
                  
                  login(req,user_)
          

                  return redirect("/")
                  
        
                
      

        
        messages.error(req, 'invalid password or email')
        return render (req,"login.html")
      
      else :
          
          messages.error(req, 'invalid data')
          return render (req,"login.html")
    else:
          
          return render (req,"login.html")
    

@api_view(["POST","GET"])
def otppassword(request):
    if(request.method=="POST"):
  
      
      dataser = passwordreset_form(request.data)
      id = randomString(4)
      
      if (dataser.isValid()):

          user_ = authenticate(request,email =request.data["email"])
          if(user_ is not None):
                send_mail("otp", f"""
  <div>
              <h1 style="color:blue">OTP code</h1>
              <p>copy the code below to proceed with password reset</p>
          
              <p>do not share this code with anybody</p>
          
              <p>OTP  {id}</p>
              <p>Thanks</p>
              <p>Technical Team</p>
          </div>

                  """, "dussy@gmail.com", [request.data["email"]])
                
                
                OTP.objects.create(otp=id,email=request.data["email"])
          else:
              messages.error(request, 'invalid email')


              return render(request,"signup.html")
      else:
          messages.error(request, 'invalid details')
          return render(request,"signup.html")
    else:
         return render(request,"otppassword.html")
               
       
              
    
    messages.error(request, 'there is an error in reseting passwrod')
    return render(request,"signup.html")
@api_view(["POST","GET"])
def passwordreset(request):
  
    if request.method =="POST":
      signupdataser = passwordotp_form(request.data)
    
      
      if (signupdataser.isValid()):
          data =OTP.objects.get(otp=request.data.otp)
          if data:
              email = data["email"]
              user_ =CustomUser.objects.get(email=request.data["email"])
              user_.set_password(request.data["password"])
              user_.save()
              data.delete()
              redirect("/login")
              
              

        
          else:
                messages.error(request, 'invalid  otp')
                return render(request,"signup.html")
              
        

      
      else:
          messages.error(request, 'invalid form values')
          return render(request,"signup.html")
          
        
                
      
      messages.error(request, 'there is an error in signing up')
      return render(request,"signup.html")
    else:
        return render(request,"passwordreset.html")
        


    
@api_view(["POST","GET"])
def signup(request):
    if request.method=="GET":
      return render(request,"signup.html")
      

    
    signupdataser = signupdata_form(request.data)
    id = randomString(12)
    
    if (signupdataser.isValid()):
        user_ =CustomUser.objects.create(email=request.data["email"],id_ =id,username=request.data["username"])
       
              
        perm = perff("org")
        user_.user_permissions.add(perm)
        user_.set_password(request.data["password"])
        user_.save()
        login(request,user_)
      

        return redirect("/")
       
              
    
    messages.error(request, 'there is an error in signing up')
    return render(request,"signup.html")
    
