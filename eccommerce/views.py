from django.shortcuts import render ,redirect
# import 

def index (req):
  if(req.user):
    print(req.user)
  return   render(req,"home.html")
def product (req):
  return   render(req,"product.html")
def reservations (req):
  return   render(req,"reservations.html")
def productlist (req):
  return   render(req,"productlist.html")
def contactus (req):
  return   render(req,"contactus.html")
def book (req):
  return   render(req,"bookreservation.html")