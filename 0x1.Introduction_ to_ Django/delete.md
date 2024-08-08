from bookshelf.models import Book

book1 = Book.objects.get(id=1)
book1.delete()

Output: Checking th available books now shows an empty list.