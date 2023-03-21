
# Create your views here.

from django.shortcuts import render,redirect,reverse,HttpResponse
from flipkart.forms import RegisterForms,FlipForm
from .models import Flipkart
from django.contrib.auth.models import User
from flipkart.forms import FlipForm,AddUser

from django.contrib import messages
from flipkart.core.helper import add_to_cart_helper,remove_from_cart_helper 
# Create your views here.


def add(request):
     form=FlipForm()
     if request.method == 'POST':
        form = FlipForm(request.POST)
        if form.is_valid():
            flip = form.save()
            flip.save()
     return render(request,'order.html',{'form': form})


def p_detail(request):
    prod = Flipkart.objects.all()
    return render(request,'details.html',{'prod':prod})






def add_user(request):
    form = AddUser()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        new = User.objects.create_user(username, password)
        new.save()
    return render(request,'new_user.html',{'form':form})













def add_to_cart(request,**kwargs):
        cart = add_to_cart_helper(request,**kwargs)
        print(cart)
        return render(request,'cart.html',{'cart':cart})

def remove_from_cart(request,**kwargs):
      var = remove_from_cart_helper(request,**kwargs)
      print(var)
      return render(request,'cart.html',{'var':var})