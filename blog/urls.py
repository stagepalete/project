from django.urls import path
from .views import Blogs, Blog, Article

urlpatterns = [
    path('blogs/', Blogs.as_view(), name='blogs'),
    path('blog/<slug:slug>/', Blog.as_view(), name='blog'),
    path('blog/<slug:blog>/<slug:article>/', Article.as_view(), name='article')
]
