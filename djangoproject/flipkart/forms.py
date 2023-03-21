


from django import forms
from flipkart.models import Flipkart

class RegisterForms(forms.Form):
    num1 = forms.CharField()
    num2 = forms.CharField()

class FlipForm(forms.ModelForm):
    class Meta:
        model = Flipkart
        fields = ['prod_name','prod_price','prod_quantity']




class AddUser(forms.Form):
    username = forms.CharField(max_length=25,label='Enter the name of User')
    password = forms.CharField(widget=forms.PasswordInput)