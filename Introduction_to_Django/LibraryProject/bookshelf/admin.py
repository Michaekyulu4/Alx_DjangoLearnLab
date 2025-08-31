from django.contrib import admin
# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")   # Show these columns in admin list
    list_filter = ("publication_year", "author")             # Filter sidebar
    search_fields = ("title", "author")                      # Search box

admin.site.register(Book)