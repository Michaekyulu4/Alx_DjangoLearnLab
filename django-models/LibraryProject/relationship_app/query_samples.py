from relationship_app.models import Author, Book, Library, Librarian


from relationship_app.models import Author, Book, Library, Librarian

def from relationship_app.models import Author, Book, Library, Librarian

def run():
    # 1. Query all books by a specific author
    author_name = "J.K. Rowling"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")

    # 2. List all books in a library
    library_name = "Central Library"
    library = None
    try:
        library = Library.objects.get(name=library_name)
        print(f"\nBooks in {library_name}:")
        for book in library.books.all():
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

    # 3. Retrieve the librarian for a library using Librarian.objects.get(library=...)
    if library:
        try:
            librarian = Librarian.objects.get(library=library)
            print(f"\nLibrarian for {library_name}: {librarian.name}")
        except Librarian.DoesNotExist:
            print(f"No librarian found for '{library_name}'.")