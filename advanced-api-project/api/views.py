from rest_framework import generics
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm
from .seriealizers import BookSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class BookListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(CreateView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    model = Book
    form_class = BookForm
    template_name = "api/book_form.html"
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    permission_classess = [IsAuthenticated]

    model = Book
    form_class = BookForm
    template_name = "api/book_form.html"
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    permission_classes = [IsAuthenticated]

    model = Book
    template_name = 'api/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
