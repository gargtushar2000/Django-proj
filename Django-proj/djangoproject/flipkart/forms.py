


from django import forms
from flipkart.models import Flipkart
from django.contrib.auth.models import User

class RegisterForms(forms.Form):
    num1 = forms.CharField()
    num2 = forms.CharField()

class FlipForm(forms.ModelForm):
    class Meta:
        model = Flipkart
        fields = ['prod_name','prod_price','prod_quantity']




class CreateNewUserForm(forms.ModelForm):
      class Meta:
            model = User
            fields = ('username','password')