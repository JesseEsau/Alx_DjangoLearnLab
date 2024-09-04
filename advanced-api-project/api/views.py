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


class BookCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(generics.UpdateAPIView):
    permission_classess = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
