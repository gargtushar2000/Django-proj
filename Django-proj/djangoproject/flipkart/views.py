


from django.shortcuts import render,redirect,reverse,HttpResponse
from flipkart.forms import RegisterForms,FlipForm
from .models import Flipkart
from django.contrib.auth.models import User
from flipkart.forms import FlipForm,CreateNewUserForm
from django.contrib import messages
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
    form = CreateNewUserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        new = User.objects.create_user(username, password)
        new.save()
    return render(request,'new_user.html',{'form':form})


def home_page(request):
    return render(request,'homepage.html', {})



def create_user(request):
    form = CreateNewUserForm()
    if request.method == 'POST':
        form = CreateNewUserForm(request.POST)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = User.objects.create_user(username=username, password=password)
        user.save()
    return render(request,'homepage.html', {'form':form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print('===========>')
        print(user)
        if user is not None:
            login(request, user)
            return redirect('details')
    return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    return redirect("details")