from eccommerce.base.models import OTP, RESERVATIONS
from eccommerce.base.utils import randomString
from .models import CART
from django.test import TestCase ,Client
from django.urls import reverse

from django.contrib.auth import get_user_model

# Create your tests here.
USER_MODEL = get_user_model()


class TestReservationModel(TestCase):
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
          
            username='user123',
            password='password456'
        )
        cls.id = randomString(12)


        cls.reservations = RESERVATIONS(resId=id,date="2024-04-21T03:59:14.474Z",room=1,table=1,email="princewillasotibe123@gmail.com")

    

    def test_create_resvation(self):
        """ Tests that a reservation model data after creation"""

        self.assertEqual(self.reservations.resId, self.id)
        self.assertEqual(self.reservations.room, 1)
        self.assertEqual(self.reservations.username, self.user.username)

    def test_reservation_str(self):
        """ Tests the __str__ of the reservation model"""

        self.assertEqual(str(self.reservation), self.reservations.username)

   

    def test_reservation_id_are_unique(self):
        """ Tests two reservation with identical titles from the same author receive different slugs """
        id = randomString(12)
        second_res = RESERVATIONS.objects.create(
            resId=id,
            date="2024-04-21T03:59:14.474Z",room=1,table=1,email="princewillasotibe123@gmail.com",
            username=self.user.username,
        )

        self.assertNotEqual(second_res.resId, self.id)


    def test_delete_reservation(self):
        """ test delete resevation model """

        RESERVATIONS.objects.delete(
            resId=self.id
           
        )
        second_title = RESERVATIONS.objects.get(
            resId=self.id
           
        )

        self.assertNotEqual(self.id, second_title.resId)



class TestOtpModel(TestCase):
    """
    Things to test:
    - Can create data
    - Does the __str__ method behave as expected?
    
    
    """

    @classmethod
    def setUpTestData(cls):
        cls.otp1=1234
        cls.otp2=2345
        cls.email ="janedoe@test.com"

        cls.otp = OTP.objects.create(
            email=cls.email,
            otp=cls.otp1
          
            
            
        )

    

    def test_create_Otp(self):
        """ Tests that a otp with a email, otpid, user  can be created"""

        self.assertEqual(self.otp.email,self.email)
    

    def test_Otp_str(self):
        """ Tests the __str__ of the otp model"""

        self.assertEqual(str(self.otp), self.email)

   

  
        """ Tests two carts with identical titles from the same author receive different slugs """

        second_title = CART.objects.create(
            name='beans',
            price='10',
            image='beans.jpg',
            productid="3",
            user_id=self.user.username,
        )

        self.assertNotEqual(self.cart.productid, second_title.productid)
class TestUserModel(TestCase):
    """
    Things to test:
    - Can be create a cart with the bare minimum of fields? (name, image and userid)
    - Does the __str__ method behave as expected?
    
    - Do two carts with the same title and user same id?
    """

    @classmethod
    def setUpTestData(cls):
        cls.email = "janedoe@test.com"
        cls.username ="user123"
        cls.password = "password456"
        cls.user = USER_MODEL.objects.create_user(
            email=cls.email,
          
            username=cls.username,
            password=cls.password
        )

    

    def test_create_User(self):
        """ Tests that a user model with a email, password,  username  can be created"""

        self.assertEqual(self.user.username, self.username)
        self.assertEqual(self.user.password, self.password)
        self.assertEqual(self.user.email, self.email)


    def test_Otp_str(self):
        """ Tests the __str__ of the user model"""

        self.assertEqual(str(self.user), self.email)

   

 

class TestRenderModel(TestCase):
    """
    Things to test:
    - test correctnes of page rendered
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
     
        # cls.client.force_login(cls.user)  
    def test_get_home(self):        
        """ Tests that a GET request works and renders the correct
            template"""   
        url = reverse("home")      
        # self.client.force_login(self.user)        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    def test_get_signup(self):        
        """ Tests that a GET request works and renders the correct
            template"""   
        url = reverse("signup")      
        # self.client.force_login(self.user)        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_get_login(self):        
        """ Tests that a GET request works and renders the correct
            template"""   
        url = reverse("login")      
        # self.client.force_login(self.user)        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
      
   
