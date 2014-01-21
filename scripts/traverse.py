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

        logger.message("file: %s" % f)
        path = os.path.join(root, f)

        md5=hashlib.md5(open(path, 'r').read()).hexdigest()
        logger.message("\tmd5: %s" % md5)
        sha1=hashlib.sha1(open(path, 'rb').read()).hexdigest()
        logger.message("\tsha1: %s" % sha1)

        result = File.objects.filter(md5=md5)
        size=os.path.getsize(path)
        logger.message("\tsize: %s bayt" % size)

        if len(result) == 0:

            logger.message("first time checking for file")
            id3_manager = ID3Manager()
            id3_manager.parse(path)
            album_name = id3_manager.get_album_name()
            logger.message("\tAlbum Name: %s" % album_name)
            album_date = id3_manager.get_album_date()
            logger.message("\tAlbum Date: %s" % album_date)
            singer_name = id3_manager.get_singer_info()
            logger.message("\tSinger: %s" % singer_name)
            song_title = id3_manager.get_song_title()
            logger.message("\tSong: %s" % song_title)

            type=fileExtension

            print type
            print path


            song_file, status = File.objects.get_or_create(path=path, size=size, md5=md5,type=fileExtension,sha1=sha1)

            try:
                album_date=int(album_date)

                album_date1=datetime.date(album_date, 02, 02)#TODO:
            except ValueError:
                pass

            try:

                album, status = Album.objects.get_or_create(name=album_name, publish_date=album_date1)
            except ValueError:
                pass

            try:
                singer, status = Singer.objects.get_or_create(name=singer_name)
            except ValueError :
                pass
            try:
                song = Song.objects.create(title=song_title, singer=singer, album=album, song_file=song_file)
            except:
                song = Song.objects.create(title=prefix, singer=singer, album=album, song_file=song_file)







        else:
            logger.message("File: %s is already checked" % (f) )




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
observer.join()







