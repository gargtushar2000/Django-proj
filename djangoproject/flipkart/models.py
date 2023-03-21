

from django.db import models
from django.conf import settings

# Create your models here.

class Flipkart(models.Model):
    prod_name = models.CharField(max_length = 100)
    prod_price = models.IntegerField()
    prod_quantity = models.IntegerField()





