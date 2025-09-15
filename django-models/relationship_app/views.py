from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book

# Function-based view
def list_books(request):
    books = Book.objects.all()
    # Updated template path
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    # Updated template path
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    relationship_app/list_books.html