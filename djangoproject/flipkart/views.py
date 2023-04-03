
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from .models import Flipkart
from django.contrib.auth.models import User
from flipkart.forms import FlipForm,CreateNewUserForm
from django.contrib import messages
#from .models import Post
from django.core.paginator import Paginator

# Create your views here.

# Add product to your cart:
def add(request):
     form=FlipForm()
     if request.method == 'POST':
        form = FlipForm(request.POST)
        if form.is_valid():
            flip = form.save()
            flip.save()
     return render(request,'order.html',{'form': form})

# Product details:
def p_detail(request):
    prod = Flipkart.objects.all()
    return render(request,'details.html',{'prod':prod})

# Creating new user:
def add_user(request): 
    form = CreateNewUserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        new = User.objects.create_user(username, password)
        new.save()
    return render(request,'new_user.html',{'form':form})

# Homepage of website:
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


# For login 
def login_user(request):
    if request.method == 'POST':
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f' Please sign in again')
    form = authenticate()
    return render(request, 'login.html', {'form':form, 'title':'log in'})



def logout_user(request):

    logout_user(request)
    return redirect("details")



# def index(request):
#     posts = Post.objects.all()  # fetching all post objects from database
#     p = Paginator(posts, 5)  # creating a paginator object
    
#     # getting the desired page number from url
    
#     page_number = request.GET.get('page')
#     try:
#         page_obj = p.get_page(page_number)  # returns the desired page object
#     except PageNotAnInteger:
#         # if page_number is not an integer then assign the first page
#         page_obj = p.page(1)
#     except EmptyPage:
#         # if page is empty then return last page
#         page_obj = p.page(p.num_pages)
#     context = {'page_obj': page_obj}
#     # sending the page object to index.html
#     return render(request, 'index.html', context)



def listing(request):
    contact_list = Flipkart.objects.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    Product_Display = paginator.get_page(page_number)
    return render(request, 'details.html', {'Product_Display': p_detail})











from rest_framework.serializers import  ModelSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Flipkart
        fields = "__all__"

class Product(ListCreateAPIView):
    queryset = Flipkart.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieve(RetrieveAPIView):
    queryset = Flipkart.objects.all()
    serializer_class = ProductSerializer
    
class Destroy(DestroyAPIView):
    queryset = Flipkart.objects.all()
    serializer_class = ProductSerializer