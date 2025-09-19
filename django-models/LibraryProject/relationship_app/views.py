from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Library, Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the LibraryProject Homepage!")
# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # must be string
    context_object_name = "library"

# Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in immediately after registration
            login(request, user)
            return redirect("home")  # Replace with your homepage or dashboard URL name
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# Login View (using Django’s built-in class-based view)
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"


# Logout View (using Django’s built-in class-based view)
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"

