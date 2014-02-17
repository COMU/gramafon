#! -*- coding: utf-8 -*-
import os
import sys
import hashlib
import datetime
from os.path import abspath, dirname
from os import getcwd
import pyglet # Play music on console
from pyglet.gl import *
import pyglet.media as media
sys.path.append(dirname(dirname(getcwd())))
from mutagen.flac import FLAC #Flac  
from mutagen.apev2 import APEv2
from mutagen.mp3 import MP3
import time
import logging
from watchdog.events import LoggingEventHandler

sys.path.append(abspath(dirname(dirname(getcwd()))))
sys.path.append(abspath(dirname(dirname(dirname(getcwd())))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'gramafon.settings'

from django.conf import settings
from gramafon.utils.logger import Logger

logger = Logger()
for root, dirs, files in os.walk(settings.ARCHIEVE_PATH):
    for f in files:

        prefix, fileExtension = os.path.splitext(f)
        if fileExtension[1:] not in list(settings.MEDIA_FORMATS):
            continue

        path = os.path.join(root, f)
	music = pyglet.media.load(path) #You need to install libavbin-dev
	player=media.Player()
    	player.queue(music)
    	player.play()
    	try:
		logger.message("\tNow: %s" % f)
		logger.message("\tLength: %s bayt" % music.duration) # music.duration is the song length	
		def exit_callback(dt):
    			pyglet.app.exit()
		pyglet.clock.schedule_once(exit_callback , music.duration) #
        	pyglet.app.run()
    	except KeyboardInterrupt:
        	player.next()







