from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# import pandas as pd
import os
import random
import string
from rest_framework.decorators import api_view  
from rest_framework.response import Response


def randomString (lenght):
    res ="".join(random.choices(string.ascii_uppercase+string.digits,k=lenght))
    return str(res)
def imagee(f):
   
   
    name = randomString(7)+f.name.replace(" ","")
    print("name",name)
    
    with open("files/"+name,"wb+") as destination:
      
        for chunk in f.chunks():
            destination.write(chunk)


   
    return name


   
      
    # send_mail(subject, message, from_email, recipient_list)
