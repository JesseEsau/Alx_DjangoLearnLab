from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

posts_url = urlpatterns = router.urls

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('', include(posts_url)),
]
