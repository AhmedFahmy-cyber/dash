from django.forms import ModelForm
from .models import Order ,Customer 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Orderform(ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


class Customerform(ModelForm):
    
    class Meta:
        model = Customer
        fields = ['name','phone','email']


class Registerform(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Loginform(ModelForm):
    
    class Meta:
        model = User
        fields = ['username','password']
