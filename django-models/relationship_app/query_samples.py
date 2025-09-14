from relationship_app.models import Author, Book, Library, Librarian

def run():
    # Create sample data if not already present
    author, _ = Author.objects.get_or_create(name="J.K. Rowling")
    book, _ = Book.objects.get_or_create(title="Harry Potter and the Sorcerer's Stone", author=author)
    library, _ = Library.objects.get_or_create(name="Central Library")
    library.books.add(book)
    librarian, _ = Librarian.objects.get_or_create(name="Jane Doe", library=library)

    # Query all books by a specific author
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[b.title for b in books_by_author]}")

    # Query all books in a library
    print(f"Books in {library.name}: {[b.title for b in library.books.all()]}")

    # Retrieve the librarian for the library
    print(f"Librarian for {library.name}: {library.librarian.name}")