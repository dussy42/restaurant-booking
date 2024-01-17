from django.db import models


from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    first_name =None
    # username = None
    
    
    last_name =None
    
    email =  models.EmailField(null=True ,blank=True,unique=True)
    username =  models.EmailField(null=True ,blank=True,unique=True)


  
    # USERNAME_FIELD = "email"
    REQUIRED_FIELDS=[]


class DummyModel(models.Model):
    
    id =  models.TextField(primary_key=True)
    class Meta:
        permissions=[("user","admin")]
    
  




class  RESERVATIONS(models.Model):

    resId=models.CharField(max_length=200,unique=True)
    date=models.CharField(max_length=200,) 
    room=models.IntegerField()
    guest=models.IntegerField()
    table=models.IntegerField()
    email=models.EmailField()

    

    




class OTP(models.Model):
    email=models.EmailField()
    otp=models.CharField(max_length=200,)
    



