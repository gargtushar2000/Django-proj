from django.contrib import admin
from .models import Flipkart


# Register your models here.




class FlipAdmin(admin.ModelAdmin):
    list_display = ['Product Name','Price','Quantity','is_ordered']
    search_fields = ['Product Name']   

   
admin.site.register(Flipkart,FlipAdmin)