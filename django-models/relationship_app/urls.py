from django.urls import path
from .views import list_books
from .views import LibraryDetailView, index, register, Login, Logout

urlpatterns = [
    path('books/', list_books),
    path('library/ <int:pk> /', LibraryDetailView.as_view(), name='library_detail'),
    path('', index, name="home"),
    path("register/", register, name="register"),
    path("login/", Login, name="login"),
    path('logout/', Logout, name="logout"),
]
