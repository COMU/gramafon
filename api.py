from tastypie.resources import ModelResource
from tastypie.constants import ALL
from web.models import Song, Album, File, Singer  # Added tastypie for rest-api

class SongResource(ModelResource): #song was called from the database 
   class Meta:
	queryset = Song.objects.all()
	resorce_name = 'song'

class AlbumResource(ModelResource): #Album was called from the database
   class Meta:
        queryset = Album.objects.all()
        resorce_name = 'album'

class FileResource(ModelResource): #File was called from the database
   class Meta:
        queryset = File.objects.all()
        resorce_name = 'file'

class SingerResource(ModelResource): #Singer was called from the database
   class Meta:
        queryset = Singer.objects.all()
        resorce_name = 'singer'


