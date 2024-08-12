from bookshelf.models import Book

# Retrieve Book using its ID
book = Book.objects.get(id=1)

# Delete the Book instance
book.delete()

# Retrieve books to check if Book was actually deleted
books = Book.objects.all()
print(books)

# Output
[]
