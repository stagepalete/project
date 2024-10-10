from django.urls import path
from .views import Home, Events, EventDetail, Artists, ArtistDetail, Galleries, GalleryDetail, Bands, BandDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('events/', Events.as_view(), name='events'),
    path('event/<slug:slug>/', EventDetail.as_view(), name='event'),
    path('artists/', Artists.as_view(), name='artists'),
    path('artist/<slug:slug>/', ArtistDetail.as_view(), name='artist'),
    path('bands/', Bands.as_view(), name='bands'),
    path('bands/<slug:slug>/', BandDetail.as_view(), name='band'),
    path('galleries/', Galleries.as_view(), name='galleries'),
    path('gallery/<slug:slug>/', GalleryDetail.as_view(), name='gallery'),
    
]
