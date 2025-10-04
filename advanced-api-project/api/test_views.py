from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = APIClient()

        # Create some books
        self.book1 = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
        self.book2 = Book.objects.create(title='Animal Farm', author='George Orwell', publication_year=1945)
        self.book3 = Book.objects.create(title='Brave New World', author='Aldous Huxley', publication_year=1932)

        # Define endpoints
        self.book_list_url = reverse('book-list')  # Adjust if using router/view name

    def test_list_books(self):
        """Test retrieving a list of books (no auth required)."""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertIn('1984', [book['title'] for book in response.data])

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create a book."""
        data = {'title': 'New Book', 'author': 'Test Author', 'publication_year': 2024}
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Test that authenticated users can create a book."""
        self.client.login(username='testuser', password='testpass123')
        data = {'title': 'New Book', 'author': 'Test Author', 'publication_year': 2024}
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.last().title, 'New Book')

    def test_update_book_authenticated(self):
        """Test that authenticated users can update a book."""
        self.client.login(username='testuser', password='testpass123')
        url = reverse('book-detail', args=[self.book1.id])
        data = {'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Nineteen Eighty-Four')

    def test_delete_book_authenticated(self):
        """Test that authenticated users can delete a book."""
        self.client.login(username='testuser', password='testpass123')
        url = reverse('book-detail', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_filter_books_by_author(self):
        """Test filtering books by author."""
        response = self.client.get(self.book_list_url, {'author': 'George Orwell'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_books(self):
        """Test searching for a book by keyword."""
        response = self.client.get(self.book_list_url, {'search': 'Brave'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Brave New World')

    def test_order_books_by_year_desc(self):
        """Test ordering books by publication year descending."""
        response = self.client.get(self.book_list_url, {'ordering': '-publication_year'})
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
