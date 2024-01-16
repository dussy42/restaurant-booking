from django import forms
class signupdata_form(forms.Form):

 username = forms.CharField()
 email = forms.EmailField() 
 password = forms.CharField() 

class logindata_form(forms.Form):

 
 email = forms.CharField() 
 password = forms.CharField() 

class reservedata_form(forms.Form):

 guest = forms.CharField()
 table = forms.EmailField() 
 room = forms.CharField() 
 date = forms.DateTimeField() 

 


class passwordotp_form(forms.Form):

 
 otp = forms.CharField() 
 password = forms.CharField() 
class passwordreset_form(forms.Form):

 
 email = forms.EmailField() 
