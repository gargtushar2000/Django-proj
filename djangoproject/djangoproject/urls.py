"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('book/', include('book.urls'))
"""



from django.contrib import admin
from django.urls import path
from book.views import create_book, list_book, update_book, delete_book
from flipkart.views import add,p_detail,add_user,create_user,login_user,logout_user,home_page,listing
from flipkart.views import Product, ProductRetrieve, Destroy



urlpatterns = [
    path('', home_page,name = 'homepage'),
    path('admin/', admin.site.urls),
    path('demo/create', create_book),
    path('demo/list', list_book),
    path('demo/<int:pk>/update', update_book),
    path('demo/<int:pk>/delete', delete_book),
    
    path('flipkart/add', add),
    path('flipkart/product', p_detail),
    path('flipkart/create', create_user),
    path('flipkart/add_user', add_user),
    path('flipkart/login', login_user),
    path('flipkart/logout', logout_user),
    path('flipkart/list', listing),

    path('create_view', Product.as_view()),
    path('retrieve/<int:pk>', ProductRetrieve.as_view()),
    path('destroy/<int:pk>', Destroy.as_view())
]