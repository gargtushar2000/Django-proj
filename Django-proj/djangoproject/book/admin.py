from django.contrib import admin
from .models import Book


# Register your models here.




class BookAdmin(admin.ModelAdmin):
    list_display = ['Name','Author','Price','is_published']
    list_filter = ['is_published']
    search_fields = ['Price']

   
admin.site.register(Book,BookAdmin) 