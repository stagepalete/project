from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Blog, Article
# Create your views here.

class Blogs(ListView):
    template_name = 'pages/blogs.html'
    model = Blog
    
class Blog(DetailView):
    template_name = 'pages/blog.html'
    model = Blog
    
class Article(DetailView):
    template_name = 'pages/article.html'
    model = Article