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
from book.views import create_book,list_book,update_book,delete_book
from flipkart.views import add,p_detail,add_to_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/create', create_book),
    path('demo/list', list_book),
    path('demo/<int:pk>/update', update_book),
    path('demo/<int:pk>/delete', delete_book),
    path('flipkart/add', add),
    path('flipkart/product', p_detail),
    path('flipkart/cart', add_to_cart)
]