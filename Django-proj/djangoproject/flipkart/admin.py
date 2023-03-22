
from django.contrib import admin
from .models import Flipkart


# Register your models here.




class FlipkartAdmin(admin.ModelAdmin):
    list_display = ['prod_name','prod_price','prod_quantity']
    search_fields = ['prod_name']   

   
admin.site.register(Flipkart,FlipkartAdmin)

