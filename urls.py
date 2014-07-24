from django.conf.urls import patterns, include, url
from tastypie.api import Api
from api import SongResource, FileResource, AlbumResource, SingerResource
album_resource = AlbumResource()
singer_resource = SingerResource()
file_resource = FileResource()
song_resource = SongResource()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'web.views.login_user'),
   # (r'^login/$', 'web.views.login_user'),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^gramafon/$', 'web.views.gramafon'),
    (r'^api/', include(song_resource.urls))	#Added song_resource for rest-api
#    (r'^api/', include(file_resource.urls))    #Added file_resource for rest_api
#    (r'^api/', include(singer_resource.urls))  #Added singer_resource for rest_api
#    (r'^api/', include(album_resource.urls)),    #Added album_resource for rest_api
)

