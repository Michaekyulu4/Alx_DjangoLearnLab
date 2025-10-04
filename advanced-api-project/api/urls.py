from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),

    # Assignment-specific URLs (no <pk>)
    path('books/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', views.BookDeleteView.as_view(), name='book-delete'),

    # Realistic REST-style endpoints (with <pk>)
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update-real'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete-real'),
]
