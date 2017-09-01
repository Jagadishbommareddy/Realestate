from django.test import TestCase
from django.test import Client
from .forms import *
class Setup_Class(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(first_name="user", last_name="customer",mobile_number=9990002221,phone_number=8885556666,email_id ="user@mp.com",address1='h.no-212', address2= '2nd lane', city= 'secunderabad', state='telangana', landmark='secondlane',  pincode=500024)
class Customer_Form_Test(TestCase):
    def test_CustomerForm_valid(self):
        form = CustomerForm(data={'first_name':"user", 'last_name': 'customer', 'mobile_number':9990002221,'phone_number':8885556666,'email_id' :"user@mp.com",'address1':'h.no-212','address2':'2nd lane','city':'secunderabad','state':'telangana','landmark':'secondlane','pincode':500024})
        self.assertTrue(form.is_valid())
    def test_CustomerForm_invalid(self):
        form = CustomerForm(data={'first_name': "las%1", 'last_name': "Cu$12", 'mobile_number':'','phone_number':'','email_id' :"",'address1': '', 'address2': '', 'city': 'secund@rabad2', 'state': 'telan&ana1','landmark': '', 'pincode': ''})
        self.assertFalse(form.is_valid())
