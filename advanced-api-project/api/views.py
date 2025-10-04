from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# -----------------------------
# 1️⃣ List View - Retrieve all books
# -----------------------------
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.
    Publicly accessible (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


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
