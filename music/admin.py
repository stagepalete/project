from django.contrib import admin

from .models import *
# Register your models here.
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('nickname', )}
    
@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('nickname',)}
    
admin.site.register(Genre)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    
@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    
admin.site.register(GalleryImage)

@admin.register(ArtistGallery)
class ArtistGalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(EventGallery)
class EventGallery(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}