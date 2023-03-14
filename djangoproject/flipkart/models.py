

from django.db import models

# Create your models here.

class Flipkart(models.Model):
    prod_name = models.CharField(max_length = 100)
    prod_price = models.IntegerField(max_length = 50)
    prod_quantity = models.IntegerField(max_length = 50)
    is_ordered = models.BooleanField(default=False)






