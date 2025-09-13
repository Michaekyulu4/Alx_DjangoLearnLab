# CRUD Operations with Book Model

This file documents the Create, Retrieve, Update, and Delete operations performed on the `Book` model using the Django shell.

---

## Create
```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book