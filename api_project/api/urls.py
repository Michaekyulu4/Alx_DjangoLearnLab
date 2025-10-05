from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the ListAPIView (previous task)
    path('books/', BookList.as_view(), name='book-list'),

    # Include automatically generated CRUD routes from the router
    path('', include(router.urls)),
]