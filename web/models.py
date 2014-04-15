from django.db import models
from tastypie.utils.timezone import now
# Create your models here.

class Album(models.Model):

    name = models.CharField(max_length=150)
    publish_date = models.IntegerField()

class Singer(models.Model):

    name = models.CharField(max_length=150)

class File(models.Model):

    path = models.CharField(max_length=200)
    size = models.FloatField()
    type = models.CharField(max_length=150)
    md5 = models.CharField(max_length=100)
    sha1 = models.CharField(max_length=100)

class Song(models.Model):

    title = models.CharField(max_length=150)
    singer = models.ForeignKey(Singer)
    album = models.ForeignKey(Album)
    song_file = models.ForeignKey(File)

