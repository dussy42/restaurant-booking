from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from .models import DummyModel

def perff(perm_name):
    content_type=ContentType.objects.get_for_model(DummyModel)
    permission = Permission.objects.get_or_create(codename=perm_name,content_type=content_type)
  
   
    return permission[0]
    # else:
    #     return Permission.objects.create(codename=perm_name,name=perm_name,content_type=content_type )
         