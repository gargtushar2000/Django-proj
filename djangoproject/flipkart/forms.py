


from django import forms
from flipkart.models import Flipkart
#from django.contrib.auth.models import CreateNewUserForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
 

class RegisterForms(forms.Form):
    num1 = forms.CharField()
    num2 = forms.CharField()

class FlipForm(forms.ModelForm):
    class Meta:
        model = Flipkart
        fields = ['prod_name','prod_price','prod_quantity']


 
class CreateNewUserForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password']