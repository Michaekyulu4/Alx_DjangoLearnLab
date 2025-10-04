from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# -----------------------------
# 1️⃣ List View - Retrieve all books
# -----------------------------
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -----------------------------
# 2️⃣ Detail View - Retrieve a single book by ID
# -----------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by its ID.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


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
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom hook to handle any extra logic before saving.
        """
        serializer.save()  # Save the new book instance


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
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Hook to customize behavior before updating an instance.
        """
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
    permission_classes = [permissions.IsAuthenticated]


# Create your views here.
