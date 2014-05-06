from tastypie.resources import ModelResource
from tastypie.constants import ALL
from web.models import Song, Album, File, Singer  # Added tastypie for rest-api
from tastypie.serializers import Serializer
from tastypie import fields 
from django.core.serializers import json
from django.utils import simplejson 

class PrettyJSONSerializer(Serializer):
    json_indent = 4
 
    def to_json(self, data, options=None):
        options = options or {}
        data = self.to_simple(data, options)
        return simplejson.dumps(data, cls=json.DjangoJSONEncoder, sort_keys=True, ensure_ascii=False, indent=self.json_indent) 

class SongResource(ModelResource): #song was called from the database
   
   class Meta:
	queryset = Song.objects.all()
	#resorce_name = 'song'
	serializer = PrettyJSONSerializer() 

class AlbumResource(ModelResource): #Album was called from the database
 
   class Meta:
        queryset = Album.objects.all()
        resorce_name = 'album'
	serializer = PrettyJSONSerializer() 

class FileResource(ModelResource): #File was called from the database
   class Meta:
        queryset = File.objects.all()
        resorce_name = 'file'

class SingerResource(ModelResource): #Singer was called from the database
   class Meta:
        queryset = Singer.objects.all()
        resorce_name = 'singer'
	serializer = PrettyJSONSerializer() 


