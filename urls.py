from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'web.views.login'),
    (r'^login/$', 'web.views.login_user'),
    (r'^gramafon/$', 'web.views.gramafon'),
    (r'^invalid/$', 'web.views.invalid'),


)

