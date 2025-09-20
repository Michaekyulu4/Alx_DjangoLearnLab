from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters on the right sidebar
    list_filter = ('author', 'publication_year')

    # Add a search box
    search_fields = ('title', 'author')

# Register the model with the custom admin
admin.site.register(Book, BookAdmin)

# Register your models here.
