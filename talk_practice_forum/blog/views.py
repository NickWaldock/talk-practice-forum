from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# def home(request):
#     return render(request, 'home.html', {})


# Lists all blog posts
class HomeView(ListView):
    model = Post
    template_name = 'home.html'


# Shows a single blog post
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article-detail.html'


# Creates a new blog post
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'
    # fields = ('title', 'subtitle', 'body')
    # fields = '__all__'