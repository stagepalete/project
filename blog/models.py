from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(to='music.Artist', on_delete=models.CASCADE)
    detail = RichTextField()
    cover = models.ImageField(upload_to='blog_covers')
    head_cover = models.ImageField(upload_to='blog_head_covers')
    
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'{self.artist.name} {self.artist.lastname}\'s blog'
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    blog = models.ForeignKey(to='blog.Blog', on_delete=models.CASCADE)
    slug = models.SlugField()
    
    def __str__(self):
        return f'{self.title} by {self.blog.artist.name} {self.blog.artist.lastname}'
    
