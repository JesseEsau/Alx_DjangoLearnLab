from relationship_app.models import Book, Library

library_name = "ALX Modern Library"
books_by_jesse = Book.objects.filter(author='Jesse Esau').values()
books_by_jesse

books = Library.objects.get(name=library_name)
books.all()

librarian = Library.objects.get(id=1)
