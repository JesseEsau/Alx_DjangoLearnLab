from bookshelf.models import Book

# Create instance of Book 
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(new_book)

# Output
<Book: 1984>


