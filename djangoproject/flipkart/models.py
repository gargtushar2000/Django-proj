

from django.db import models
from django.conf import settings

# Create your models here.

class Flipkart(models.Model):
    prod_name = models.CharField(max_length = 100)
    prod_price = models.IntegerField()
    prod_quantity = models.IntegerField()
    


























# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     image = models.ImageField(null=True,Blank=True)
#     description = models.CharField(max_length=300)


# class Order(models.Model):
#     product = models.ForeignKey( Product,null=True, on_delete=models.SET_NULL)
#     customer = models.ForeignKey(Flipkart,null=True, on_delete=models.SET_NULL)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20,default= 'PENDING')