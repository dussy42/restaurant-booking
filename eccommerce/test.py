from .models import CART
from django.test import TestCase ,Client
from django.urls import reverse

from django.contrib.auth import get_user_model

# Create your tests here.
USER_MODEL = get_user_model()


class TestCartModel(TestCase):
    """
    Things to test:
    - Can be create a cart with the bare minimum of fields? (name, image and userid)
    - Does the __str__ method behave as expected?
    
    - Do two carts with the same title and user same id?
    """

    @classmethod
    def setUpTestData(cls):
        cls.user = USER_MODEL.objects.create_user(
            email='janedoe@test.com',
            first_name='Jane',
            last_name='Doe',
            username='user123',
            password='password456'
        )

        cls.cart = CART.objects.create(
            name='rice',
            image='rice.jpg',
            price="20",
            productid="2",
            
            user_id=cls.user.username,
        )

    def test_create_cart(self):
        """ Tests that a cart with a title, body, user and creation date can be created"""

        self.assertEqual(self.cart.name, 'rice')
        self.assertEqual(self.cart.user_id, self.user.username)

    def test_cart_str(self):
        """ Tests the __str__ of the cart model"""

        self.assertEqual(str(self.cart), 'usercart')

   

    def test_id_are_unique(self):
        """ Tests two carts with identical titles from the same author receive different slugs """

        second_title = CART.objects.create(
            name='beans',
            price='10',
            image='beans.jpg',
            productid="3",
            user_id=self.user.username,
        )

        self.assertNotEqual(self.cart.productid, second_title.productid)


class TestRenderModel(TestCase):
    """
    Things to test:
    - Can be create a cart with the bare minimum of fields? (name, image and userid)
    - Does the __str__ method behave as expected?
    
    - Do two carts with the same title and user same id?
    """

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = USER_MODEL.objects.create_user(
            email='janedoe@test.com',
            first_name='Jane',
            last_name='Doe',
            username='user123',
            password='password456'
        )
        cls.cart = CART.objects.create(
            name='rice',
            image='rice.jpg',
            price="20",
            productid="2",
            
            user_id=cls.user.username,
        )
        # cls.client.force_login(cls.user)  
    def test_get_home(self):        
        """ Tests that a GET request works and renders the correct
            template"""   
        url = reverse("home")      
        # self.client.force_login(self.user)        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    def test_get_productlist(self):        
        """ Tests that a GET request works and renders the correct
            template"""   
        url = reverse("productlist")      
        # self.client.force_login(self.user)        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'productlist.html')

    def test_get_cart(self):        
        """ Tests that a GET request works and renders the correct
            template"""   
        url = reverse("cart")      
        # self.client.force_login(self.user)        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
      
   
