from django.urls import path
from .views import list_books
from .views import LibraryDetailView, admin_view, librarian_view, member_view
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('books/', list_books, name="books_list"),
    path('library/ <int:pk> /', LibraryDetailView.as_view(), name='library_detail'),

    path('', views.index, name="home"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html",
         next_page="home"), name="login"),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html",
         next_page="home"), name="logout"),

    path("admin/", admin_view, name="admin"),
    path("librarian/", librarian_view, name="librarian"),
    path("member/", member_view, name="member"),


    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),



]
