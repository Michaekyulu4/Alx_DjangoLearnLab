from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from rest_framework import generics, filters
from django_filters import rest_framework
# -----------------------------
# 1️⃣ List View - Retrieve all books
# -----------------------------
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books with advanced query capabilities:
    - Filtering by title, author, and publication_year.
    - Searching by title and author name.
    - Ordering by title or publication_year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering options (fields the user can filter by)
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Search options (fields used for keyword search)
    search_fields = ['title', 'author__name']

    # Ordering options (fields that can be used to sort results)
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default order


# -----------------------------
# 2️⃣ Detail View - Retrieve a single book by ID
# -----------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by its ID.
    Publicly accessible (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -----------------------------
# 3️⃣ Create View - Add a new book
# -----------------------------
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book entry.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook for pre-save customization.
        """
        serializer.save()


# -----------------------------
# 4️⃣ Update View - Modify an existing book
# -----------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book entry.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


# -----------------------------
# 5️⃣ Delete View - Remove a book
# -----------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book entry.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
