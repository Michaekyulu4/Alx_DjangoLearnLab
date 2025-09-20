# bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from .forms import SearchForm

# View all books (requires can_view)
@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, "bookshelf/list_books.html", {"books": books})

# Create a book (requires can_create)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        year = request.POST.get("publication_year")
        Book.objects.create(title=title, author=author, publication_year=year)
        return redirect("list_books")
    return render(request, "bookshelf/create_book.html")

# Edit a book (requires can_edit)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("publication_year")
        book.save()
        return redirect("list_books")
    return render(request, "bookshelf/edit_book.html", {"book": book})

# Delete a book (requires can_delete)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/list_books.html", {"books": books})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "bookshelf/confirm_delete.html", {"book": book})



@csrf_protect
def search_books(request):
"""Secure search view using Django forms and ORM (no raw SQL)."""
form = SearchForm(request.GET or None)
results = None
if form.is_valid():
q = form.cleaned_data['query']
# Use ORM lookups and Q objects; these are parameterized by Django
results = (
Book.objects
.filter(
Q(title__icontains=q) | Q(author__name__icontains=q)
)
.distinct()
)
return render(request, 'bookshelf/book_list.html', {'form': form, 'books': results})

# If you absolutely must use raw SQL, always pass params separately
from django.db import connection


def unsafe_example_rawsql(request):
q = request.GET.get('q', '')
# BAD: string formatting into a query -> vulnerable to SQL injection
# GOOD: parameterized raw query
sql = "SELECT id, title FROM bookshelf_book WHERE title ILIKE %s"
param = ['%' + q + '%']
with connection.cursor() as cursor:
cursor.execute(sql, param) # parameters are safe
rows = cursor.fetchall()
# convert rows to model-like objects or ids then fetch via ORM if necessary
return render(request, 'bookshelf/book_list.html', {'books_raw': rows})