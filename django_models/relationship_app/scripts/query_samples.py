from relationship_app.models import Author, Book, Library, Librarian

def run():
    # 1. Query all books by a specific author
    author_name = "J.K. Rowling"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"\nBooks by {author.name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")

    # 2. List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        print(f"\nBooks in {library.name}:")
        for book in library.books.all():
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

    # 3. Retrieve the librarian for a library
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"\nThe librarian for {library.name} is {librarian.name}.")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print(f"No librarian found for '{library_name}'.")