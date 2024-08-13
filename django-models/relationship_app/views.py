from django.shortcuts import render
from .models import Book, Library
from django.views.generic import ListView

# Create your views here.


def list_books(request):
    books = Book.objects.all()
    context = {
        'book_list': books,
    }
    return render(request, "relationship_app/list_books.html", context)


class LibraryDetailView(ListView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    queryset = Library.objects.all()
