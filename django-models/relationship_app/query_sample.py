from relationship_app.models import Book, Library

books_by_jesse = Book.objects.filter(author='Jesse Esau').values()
books_by_jesse

all_books = Library.objects.all()
all_books

librarian = Library.objects.get(id=1)
librarian
