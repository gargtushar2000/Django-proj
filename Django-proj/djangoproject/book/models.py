

from django.db import models


# Create your models here.

class Book(models.Model):
    Name = models.CharField(max_length=100)
    Author = models.CharField(max_length=150)
    Price = models.TextField()
    is_published = models.BooleanField(default=False)
    #published_on = models.DateTimeField(auto_now=True)

