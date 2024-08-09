from bookshelf.models import Book

# Retrieve book
book1 = Book.objects.get(id=1)

# Udate the title of the retrieved book
book1.title = "Nineteen Eighty-Four"
book1.save()
print(book1)

# Output 
<Book: Nineteen Eighty-Four>