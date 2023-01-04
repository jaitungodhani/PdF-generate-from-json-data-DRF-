from django.contrib import admin
from .models import Author, Book
# Register your models here.

class Authoradmin(admin.ModelAdmin):
    search_fields= ['name', 'coutry']
    list_filter=['name', 'coutry']
    list_display = ['name','coutry'] 
admin.site.register(Author, Authoradmin)

class Bookadmin(admin.ModelAdmin):
    def author(self,obj):
        return obj.author.name

    search_fields= ['name', 'pub_year']
    list_filter=['name', 'pub_year']
    list_display = ['name','pub_year','author'] 
admin.site.register(Book, Bookadmin)