"""eccommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # path("account/",include("allauth.urls")),
    path("",views.index,name="home"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("reservations",views.reservations,name="reservations"),
    path("contactus",views.contactus,name="contactus"),
    path("aboutus",views.contactus,name="aboutus"),
    path("book",views.book,name="book"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
