from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {})


# Lists all blog posts
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-post_date']


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


# Updates a blog post
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update-post.html'
    # fields = ['title', 'subtitle', 'body']


# Adds a category to the category list
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add-category.html'
    fields = '__all__'


# Deletes a blog post
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')