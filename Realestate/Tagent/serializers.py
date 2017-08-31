from rest_framework import serializers
from . models import Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =['customer_id','first_name','last_name','mobile_number','phone_number','email_id','address1','address2','city','state','landmark','pincode']


