from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            events = Event.objects.all().order_by('-date'),
        )
        return context
    
class Events(ListView):
    template_name = 'pages/events.html'
    model = Event
    context_object_name = 'events'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            
        )
        return context
    
class EventDetail(DetailView):
    template_name = 'pages/event.html'
    model = Event
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'event'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            testimonies = EventTestimony.objects.filter(event=self.object.id),
            galleries = EventGallery.objects.filter(event=self.object.id)
        )
        return context
    
class Artists(ListView):
    # Includes Bands
    template_name = 'pages/artists.html'
    model = Artist
    context_object_name='artists'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            
        )
        return context
    
class ArtistDetail(DetailView):
    # Includes Bands
    template_name = 'pages/artist.html'
    model = Artist
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'artist'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            songs = Song.objects.filter(Q(band__members=self.object.id) | Q(artist=self.object.id)).distinct(),
            albums = Album.objects.filter(Q(band__members=self.object.id) | Q(artist=self.object.id)).distinct(),
            events = Event.objects.filter(Q(bands__members=self.object.id) | Q(artists=self.object.id)).distinct(),
            galleries = ArtistGallery.objects.filter(Q(band__members=self.object.id) | Q(artist=self.object.id)).distinct(),
        )
        return context

class Bands(ListView):
    template_name = 'pages/bands.html'
    model = Band
    context_object_name = 'bands'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            
        )
        return context
    
class BandDetail(DetailView):
    template_name = 'pages/band.html'
    model = Band
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'band'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            songs = Song.objects.filter(band=self.object.id),
            albums = Album.objects.filter(band=self.object.id),
            events = Event.objects.filter(bands=self.object.id)
        )
        return context
    
class Galleries(ListView):
    template_name = 'pages/galleries.html'
    model = ArtistGallery
    context_object_name = 'galleries'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            
        )
        return context
    


class GalleryDetail(DetailView):
    template_name = 'pages/gallery.html'
    model = ArtistGallery
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'gallery'

    def get_object(self):
        # Try to get the object from ArtistGallery first
        try:
            return ArtistGallery.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        except ArtistGallery.DoesNotExist:
            # If not found, fall back to EventGallery
            try:
                return EventGallery.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
            except EventGallery.DoesNotExist:
                # If neither is found, raise a 404 error
                raise Http404("Gallery not found")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # The 'gallery' context will already have the object from get_object
        return context
