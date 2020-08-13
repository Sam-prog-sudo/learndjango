from django.urls import path

from .views import PostsPageView, CreatePostView

urlpatterns = [
    path('', PostsPageView.as_view(), name='posts'),
    path('new_post/', CreatePostView.as_view(), name='add_post'),
]
