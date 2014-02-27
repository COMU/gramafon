from django.conf.urls import patterns, include, url
from api import SongResource

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
)

