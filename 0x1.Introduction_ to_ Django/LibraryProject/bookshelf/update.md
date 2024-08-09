from bookshelf.models import Book

book1 = Book.objects.get(id=1)

book1.title = "Nineteen Eighty-Four"
book1.save()

#checking the avalible books now reflects the new name.

Output: <QuerySet [<Book: Nineteen Eighty-Four By George Orwell in 1949>]>