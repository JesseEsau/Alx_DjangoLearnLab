from relationship_app.models import Book, Library, Author

# variables
library_name = "ALX Modern Library"
author_name = "Jesse Esau"

# get all books by a specific author
author = Author.objects.get(name=author_name)
books_by_jesse = Book.objects.filter(name=author)

# Retrieve all books from a given library
books = Library.objects.get(name=library_name)
books.all()

# Retrieve librarian of a library
librarian = Library.objects.get(id=1)
