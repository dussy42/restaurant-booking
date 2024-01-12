from django.db import models




class  PRODUCT(models):

    product_image_name:models.CharField()
    product_name:models.CharField()
    product_price:models.CharField()
    product_description:models.CharField()
    

    




class CART(models):
    user_id:models.CharField()
    product:models.ManyToManyField(PRODUCT)
    



