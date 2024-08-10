from bookshelf.models import Book

# Retrieve Book using its ID
book1 = Book.objects.get(id=1)

# Delete the Book instance
book1.delete()

# Retrieve books to check if Book was actually deleted
books = Book.objects.all()
print(books)

# Output
[]
