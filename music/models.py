from django.db import models
from ckeditor.fields import RichTextField
from djmoney.models.fields import MoneyField

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='artist_cover', blank=True)
    
    detail = RichTextField()
    biographyh = RichTextField()
    nickname = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField()
    origin = models.CharField(max_length=255)
    years_of_activity = models.CharField(max_length=50, verbose_name='Годы активности')
    labels = models.ForeignKey(to='music.Label', on_delete=models.CASCADE)
    awards = models.CharField(max_length=50, blank=True)
    
    is_band_member = models.BooleanField(default=False)
    
    website = models.URLField(blank=True)
    
    slug = models.SlugField()
    
    def __str__(self):
        return f'{self.name} {self.lastname} ({self.nickname})'
    
class Band(models.Model):
    nickname = models.CharField(max_length=50)
    detail = RichTextField()
    cover = models.ImageField(upload_to='band_cover', blank=True)
    
    origin = models.CharField(max_length=255)
    years_of_activity = models.CharField(max_length=50, verbose_name='Годы активности')
    labels = models.ForeignKey(to='music.Label', on_delete=models.CASCADE)
    awards = models.CharField(max_length=50, blank=True)
    members = models.ManyToManyField(to='music.Artist')
    
    website = models.URLField(blank=True)
    
    slug = models.SlugField()
    
    def __str__(self):
        return f'{self.nickname}'
    
class Genre(models.Model):
    genre = models.CharField(max_length=59)
    
    def __str__(self):
        return f'{self.genre}'
    
class Song(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='song_covers')
    
    lyrics = RichTextField(blank=True)
    genre = models.ForeignKey(to='music.Genre', on_delete=models.CASCADE)
    artist = models.ManyToManyField(to='music.Artist')
    band = models.ManyToManyField(to='music.Band')
    length = models.TimeField()
    song_writers = models.CharField(max_length=100, blank=True)
    producer = models.CharField(max_length=100)
    video_url = models.URLField(blank=True)
    released = models.DateField()
    
    slug = models.SlugField()
    
    def __str__(self):
        return f'{self.name} by {self.artist.first}'
    
    
class Album(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='album_covers')
    artist = models.ManyToManyField(to='music.Artist')
    band = models.ManyToManyField(to='music.Band')
    
    detail = RichTextField(blank=True)
    
    released = models.DateField()
    recorder = models.CharField(max_length=30, blank=True)
    length = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    songs = models.ManyToManyField(to='music.Song')
    
    slug = models.SlugField()
    
    def __str__(self):
        return f'{self.name} album by {self.artist.first}'

class Label(models.Model):
    name = models.CharField(max_length=100)
    company_cover = models.ImageField(upload_to='company_covers', blank=True)
    detail = RichTextField(blank=True)
    founded_date = models.DateField()
    founders = models.CharField(max_length=255, blank=True)
    headquarters = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    
    COMPANY_TYPE_CHOICES = {
        'private' : 'Private',
        'public' : 'Public'
    }
    company_type = models.CharField(max_length=50, choices=COMPANY_TYPE_CHOICES)
    
    slug = models.SlugField()
    
    def __str__(self):
        return f'{self.name} label'

class ArtistGallery(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='gallery_covers')
    detail = RichTextField()
    images = models.ManyToManyField(to='music.GalleryImage')
    artist = models.ForeignKey(to='music.Artist', on_delete=models.CASCADE, blank=True, null=True)
    band = models.ForeignKey(to='music.Band', on_delete=models.CASCADE, blank=True, null=True)
    
    slug = models.SlugField()
    
    def __str__(self):
        if self.artist:
            return f'Gallery of {self.artist.name} {self.artist.lastname}'
        elif self.band:
            return f'Gallery of {self.band.nickname}'
        return f'Gallery: {self.name}'
    
class EventGallery(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='event_covers')
    detail = RichTextField()
    images = models.ManyToManyField(to='music.GalleryImage')
    event = models.ForeignKey(to='music.event', on_delete=models.CASCADE)
    
    slug = models.SlugField()
    
    def __str__(self):
        return f'Gallery: {self.name}, {self.event.name}'

class GalleryImage(models.Model):
    name = models.CharField(max_length=100)
    detail = RichTextField()
    mediafile = models.FileField(upload_to='gallery_images')
    
    published = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Photo {self.name} - {self.mediafile.name}'
    

class Event(models.Model):
    name = models.CharField(max_length=100)
    artists = models.ManyToManyField(to='music.Artist', blank=True)
    bands = models.ManyToManyField(to='music.Band', blank=True)
    
    poster = models.ImageField(upload_to='event_poster')
    detail = RichTextField()
    
    venue = models.CharField(max_length=255)
    date = models.DateField()
    start = models.TimeField()
    
    STATUS = {
        'Отменено' : 'Отменено',
        'Прошло' : 'Прошло',
        'Ожидается' : 'Ожидается',
    }
    status = models.CharField(max_length=100, choices=STATUS, default='Ожидается')
    
    PARKING = {
        'Есть' : 'Есть',
        'Нет' : 'Нет',
    }
    parking = models.CharField(max_length=100, choices=PARKING, default='Есть')
    duration = models.CharField(max_length=29, default='3 Часа')
    
    AGE = {
        '12+' : '12+',
        '16+' : '16+',
        '18+' : '18+',
        '21+' : '21+'
    }
    age_restriction = models.CharField(max_length=29, choices=AGE)
    
    slug = models.SlugField()
    
    def __str__(self):
        return f'{self.name}'
    
class EventTestimony(models.Model):
    event = models.ForeignKey(to='music.Event', on_delete=models.CASCADE)
    testimony = RichTextField()
    
    date = models.DateField()
    
    def __str__(self):
        return f'{self.event.name} - {self.date}'

class Ticket(models.Model):
    event = models.ForeignKey(to='music.Event', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = RichTextField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='KZT')
    AGE = {
        'Десткий' : 'Десткий',
        'Взрослый' : 'Взрослый',
        'Студенческий' : 'Студенческий',
    }
    ticket_type = models.CharField(max_length=29)
    
    def __str__(self):
        return f'{self.event.name}({self.ticket_type}) - {self.price}'
    
class AfterParty(models.Model):
    event = models.ForeignKey(to='music.Event', on_delete=models.CASCADE)
    sold_tickets = models.ManyToManyField(to='music.Ticket')
    