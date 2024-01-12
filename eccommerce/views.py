from django.shortcuts import render ,redirect
# import 

def index (req):
  if(req.user):
    print(req.user)
  return   render(req,"index.html")
def product (req):
  return   render(req,"product.html")
def cart (req):
  return   render(req,"cart.html")
def productlist (req):
  return   render(req,"productlist.html")