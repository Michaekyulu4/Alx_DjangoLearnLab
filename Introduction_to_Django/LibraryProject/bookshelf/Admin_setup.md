# Django Admin Integration for Book Model

This document describes how the `Book` model was integrated into the Django Admin interface and customized for better usability.

---

## Registering the Book Model
In `bookshelf/admin.py`, the `Book` model was registered with a custom `BookAdmin` class:

```python
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("publication_year", "author")
    search_fields = ("title", "author")

admin.site.register(Book, BookAdmin)