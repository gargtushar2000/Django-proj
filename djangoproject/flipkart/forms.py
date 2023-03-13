


from django import forms
from flipkart.models import Flipkart

class RegisterForms(forms.Form):
    num1 = forms.CharField()
    num2 = forms.CharField()

class FlipForm(forms.ModelForm):
    class Meta:
        model = Flipkart
        fields = ['Product Name','Price','Quantity','is_ordered']