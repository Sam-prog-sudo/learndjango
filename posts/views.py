from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post


class PostsPageView(ListView):
    model = Post
    template_name = 'posts.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'new_post.html'
    success_url = reverse_lazy('posts')
