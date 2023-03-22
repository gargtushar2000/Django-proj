


from django import forms
from book.models import Book

class RegisterForms(forms.Form):
    num1 = forms.CharField()
    num2 = forms.CharField()

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Name','Author','Price','is_published']