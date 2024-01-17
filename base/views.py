from django.shortcuts import render ,redirect
from rest_framework.decorators import api_view 
from .utils import randomString 
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required ,permission_required
from .permissions import perff
from django.contrib.auth import authenticate ,login,logout
from .models import CustomUser ,OTP ,RESERVATIONS
from .serialisers import resser ,otpser
# from ..eccommerce.backend import EmailBackend
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
  ress = CustomUser.objects.get(email=req.user.email)
  data =  resser(res,many=True)
  # print(res,ress,data.data)
  for val in data.data:
      print(val["email"],"Asa")
  print([dict(_) for  _  in data.data])
  # print(res)
  return   render(req,"reservations.html",{"res" :data.data})



@api_view(["GET"])
def contactus (req):
  return   render(req,"contactus.html")

@login_required(login_url="/login")
@api_view(["GET","POST"])
def book (req):
  print("kdkdkddk")
  if(req.method=="POST"):
    data = reservedata_form(req.POST)
    print(req.POST,data.is_valid())
    if(data.is_valid()):
        id = randomString(12)
        i = req.POST
        print(id)
        print(i["guest"])
        RESERVATIONS.objects.create(guest=i["guest"],table= i["table"],room=i["room"], date=i["date"], resId=id,email=req.user.email)
        # messages.info(req, f"""resevrtions booked  
        #               reservation id {id}
        #               """)

    
        # return   render(req,"message.html",success="/")
        return   redirect("/reservations")
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
def deleteres (req,id):
  print(id)
  data  =RESERVATIONS.objects.get(resId=id)
  data.delete()

  return   render(req,"reservations.html")

# @api_view(["POST"])
# @login_required(login_url="/login")
# # @permission_required("user")
# def bookreserve (req):
  



@api_view(["POST","GET"])
@login_required(login_url="/login")
def logout_(req):
    logout(req)
    return redirect("/")
    


@api_view(["POST","GET"])
def login_(req):
    print(req.method,"Sss")
    if req.method=="POST":
  
   
      dataser = logindata_form(req.POST)
      print(req.POST,dataser.is_valid(),req.POST["email"])
      if(dataser.is_valid()):  

      
      
        user_ = authenticate(req,email =req.POST["email"],password=req.POST["password"])
        print(user_,"Sdsd")
  
      
        if (user_ is not None):
          
                  
                  
                  login(req,user_,backend="eccommerce.backend.EmailBackend")
          

                  return redirect("/")
                  
        
                
      

        
        messages.error(req, 'invalid password or email')
        return render (req,"login.html")
      
      else :
          
          messages.error(req, 'invalid data')
          return render (req,"login.html")
    else:
          if req.user.is_authenticated:
           return redirect("/")
          
          return render (req,"login.html")
    

@api_view(["POST","GET"])
def passwordotp(request):
    if(request.method=="POST"):
  
      
      dataser = passwordreset_form(request.POST)
      id = randomString(4)
      
      if (dataser.is_valid()):
          
          l =f"""
            <div>
                        <h1 style="color:blue">OTP code</h1>
                        <p>copy the code below to proceed with password reset</p>
                    
                        <p>do not share this code with anybody</p>
                    
                        <p>OTP  </p>
                        <p>Thanks</p>
                        <p>Technical Team</p>
                    </div>

                            """
          user_ = CustomUser.objects.get(email =request.POST["email"])
          if(user_ ):
                print(user_,"SDsd")
                send_mail(subject="otp", message="otp",html_message=f"""
            <div>
                        <h1 style="color:blue">OTP code</h1>
                        <p>copy the code below to proceed with password reset</p>
                    
                        <p>do not share this code with anybody</p>
                    
                        <p>OTP {id} </p>
                        <p>Thanks</p>
                        <p>Technical Team</p>
                    </div>

                            """, from_email="princewillasotibe234@gmail.com",recipient_list= [request.POST["email"]])
                
                
                
                OTP.objects.create(otp=id,email=request.POST["email"])
                return redirect("/passwordreset")
                
          else:
              messages.error(request, 'invalid email')


              return render(request,"passwordotp.html")
      else:
          messages.error(request, 'invalid details')
          return render(request,"passwordotp.html")
    else:
         if request.user.is_authenticated:
          return redirect("/")
         return render(request,"passwordotp.html")
               
       
              
    
  #   messages.error(request, 'there is an error in reseting passwrod')
  #  return render(request,"signup.html")
@api_view(["POST","GET"])
def passwordreset(request):
  
    if request.method =="POST":
      signupdataser = passwordotp_form(request.POST)
    
      
      if (signupdataser.is_valid()):
          data_ = OTP.objects.get(otp=request.POST["otp"])
          if data_:
              data = otpser(data_).data
              email = data["email"]
              user_ =CustomUser.objects.get(email=email)
              user_.set_password(request.POST["password"])
              user_.save()
              data_.delete()
              return redirect("/login")
              
              

        
          else:
                messages.error(request, 'invalid  otp')
                return render(request,"passwordreset.html")
              
        

      
      else:
          messages.error(request, 'invalid form values')
          return render(request,"passwordreset.html")
          
        
                
      
      # messages.error(request, 'there is an error in signing up')
      # return render(request,"passwordreset.html")
    else:
        if request.user.is_authenticated:
         return redirect("/")
        return render(request,"passwordreset.html")
        


    
@api_view(["POST","GET"])
def signup(request):
    if request.method=="GET":
      if request.user.is_authenticated:
        return redirect("/")
    # print(request.user.is_authenticated())
      return render(request,"signup.html")
      

    
    print("lllbmbmb")
    signupdataser = signupdata_form(request.POST)
    
    if (signupdataser.is_valid()):
        print("lll",request.POST)
        user_ =CustomUser.objects.create(email=request.POST["email"],username=request.POST["username"])
       
              
        # perm = perff("org")
        # user_.user_permissions.add(perm)
        user_.set_password(request.POST["password"])
        user_.save()
        print("kkk")
        login(request,user_,backend="eccommerce.backend.EmailBackend")
        print("kkkllll")
      

        return redirect("/")
       
              
    
    messages.error(request, 'there is an error in signing up')
  
        
    return render(request,"signup.html")
    
