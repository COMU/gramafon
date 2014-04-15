#! -*- coding: utf-8 -*-
import os
import sys
import hashlib
import datetime
from os.path import abspath, dirname
from os import getcwd
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
sys.path.append(dirname(dirname(getcwd())))
from mutagen.flac import FLAC #Flac  
from mutagen.apev2 import APEv2
from mutagen.mp3 import MP3
from gramafon.utils.id3.handler import *
import time
import logging
from watchdog.events import LoggingEventHandler

sys.path.append(abspath(dirname(dirname(getcwd()))))
sys.path.append(abspath(dirname(dirname(dirname(getcwd())))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'gramafon.settings'

from django.conf import settings
from gramafon.web.models import File,Singer,Album, Song
from gramafon.utils.id3.handler import MP3FileInfo as ID3Manager
from gramafon.utils.logger import Logger

logger = Logger()

logger.message("Path: %s" % settings.ARCHIEVE_PATH)
for root, dirs, files in os.walk(settings.ARCHIEVE_PATH):
    for f in files:

        prefix, fileExtension = os.path.splitext(f)
        if fileExtension[1:] not in list(settings.MEDIA_FORMATS):
            continue

        path = os.path.join(root, f)
	md5=hashlib.md5(open(path, 'r').read()).hexdigest()
	sha1=hashlib.sha1(open(path, 'rb').read()).hexdigest()

        result = File.objects.filter(md5=md5)
        size=os.path.getsize(path)
        logger.message("\tsize: %s bayt" % size)
	
	if len(result) == 0:

            logger.message("File: %s is first checked" % (f) )
            id3_manager = ID3Manager()
            id3_manager.parse(path)
	    try:	
            	album_name = id3_manager.get_album_name()
            	logger.message("\tAlbum Name: %s" % album_name)
	    except:
		album_name = ""
                logger.message("\tAlbum Name: %s" % album_name)

	    try:	
            	album_year = id3_manager.get_album_year()
            	logger.message("\tAlbum Year: %s" % album_year)
	    except:
		album_year = 0
                logger.message("\tAlbum Year: %s" % album_year)

            try:
	    	singer_name = id3_manager.get_singer_info()
            	logger.message("\tSinger: %s" % singer_name)
	    except:
		singer_name = ""
                logger.message("\tSinger: %s" % singer_name)

            try:
	    	song_title = id3_manager.get_song_title()
            	logger.message("\tSong: %s" % song_title)
	    except:
                song_title = ""
                logger.message("\tSong: %s" % song_title)


            type=fileExtension

            song_file, status = File.objects.get_or_create(path=path, size=size, md5=md5,type=fileExtension,sha1=sha1)

            try:
                singer, status = Singer.objects.get_or_create(name=singer_name)
            except ValueError :
                pass
	
	    album, status = Album.objects.get_or_create(name=album_name, publish_date=album_year)
            
	    try:
		song = Song.objects.create(title=song_title, singer=singer, album=album, song_file=song_file)
	    except:
		song = Song.objects.create(title=prefix, singer=singer, album=album, song_file=song_file)

	else:
            logger.message("File: %s is already checked" % (f) )







