from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Register, Login, ProfileView, NewPost, Posts, PostDetail, PostEdit, PostDelete

from .views import CommentCreateView, CommentListView, CommentUpdateView, CommentDeleteView
urlpatterns = [
    path('register/', Register.as_view(), name="regiser"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('profile/', ProfileView, name="profile"),

    # Posts
    path('posts/', Posts.as_view(), name="posts"),
    path('posts/<int:pk>/', PostDetail, name="post_detail"),
    path('post/<int:pk>/update/', PostEdit.as_view(), name="post_edit"),
    path('post/new/', NewPost.as_view(), name='new_post'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name="post_delete"),

    # Comments
    path("posts/<int:post_id>/comments/new/",
         CommentCreateView, name="new_comment"),
    path("posts/<int:pk>/comments/",
         CommentListView.as_view(), name="comment_list"),
    path("post/<int:post_id>/comment/<int:pk>/update/",
         CommentUpdateView.as_view(), name="edit_comment"),
    path("post/<int:post_id>/comment/<int:pk>/delete/",
         CommentDeleteView.as_view(), name="delete_comment"),


    # path("post/<int:pk>/comment/detail/<int:pk>/",
    #      CommentDetailView.as_view(), name="comment_detail"),
]
