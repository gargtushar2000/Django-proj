

from django.db import models


# Create your models here.
 
class Book(models.Model):
    Name = models.CharField(max_length=100)
    Author = models.CharField(max_length=150)
    Price = models.CharField(max_length=50)
    is_published = models.BooleanField(default=False)

   