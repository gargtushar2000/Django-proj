from django.contrib import admin
from .models import Book
# from datetime import timedelta
# from django.utils import timezone

# Register your models here.




class BookAdmin(admin.ModelAdmin):
    list_display = ['Name','Author','Price','is_published']
    list_filter = ['is_published']
    search_fields = ['Price']


    # def is_recently_published(self,obj):
    #     if obj.is_publishe==True:
    #         var = obj.published_on  
    #         now_time = timezone.now() 
    #         blog_end_time = now_time + timezone.timedelta(days=2) #two days after present date
    #         blog_start_time = now_time - timezone.timedelta(days=2) #two days before present date
    #         if  var > blog_start_time and var < blog_end_time:
    #             return True
    #         else:
    #             return False
    #     pass
   
admin.site.register(Book,BookAdmin)