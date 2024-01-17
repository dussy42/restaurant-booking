
from .models import RESERVATIONS,OTP
from rest_framework.serializers import  ModelSerializer
class resser (ModelSerializer):
     class Meta:
        model = RESERVATIONS
        fields = '__all__'
class otpser (ModelSerializer):
     class Meta:
        model = OTP
        fields = '__all__'
