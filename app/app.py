import eyed3
from flask import Flask, render_template, request
import pygame
import os
import json
import random

# from tinytag import TinyTag
# from mutagen.mp3 import MP3


# import ipdb
# from mutagen.mp3 import MP3

app = Flask(__name__)
songs_path = "/home/burcin/song/song/"
sarki = songs_path + "01.TheCrushOfLove.mp3"
songs = os.listdir(songs_path)


# tag = TinyTag.get("sarki") print("This track is by %s." % tag.artist) print("It is %f seconds long." % tag.duration)

@app.route("/")
def song_information():
    song_info_list = []
    print (
        "********************************************************************************************************")
    duration = eyed3.load(sarki).info.time_secs
    print(duration)
    for song in songs:
        if song.endswith(".mp3"):
            path = songs_path + song
            audiofile = eyed3.load(path)
            song_info = {'artist': audiofile.tag.artist, 'album': audiofile.tag.artist,
                         'title': audiofile.tag.title, 'path': path, 'genre': audiofile.tag.genre}
            song_info_list.append(song_info)
    return render_template("index.html", song_info_list=song_info_list)


@app.route("/play", methods=['POST'])
@app.route("/randomList", methods=['POST'])
def play():
    if request.path == '/play':
        request_body = json.loads(request.get_data())
        song_path = request_body['song']
        pygame.init()
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        print(song_path)
        # bir kere cal. play(-1) sonsuz cal
        return "play basarili"
    if request.path == '/randomList':
        random_song = random.choice(songs)
        print (songs_path + random_song)
        path = songs_path + random_song
        pygame.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        return "random basarili"
    return "basarili"


@app.route("/stop", methods=['POST'])
def stop():
    pygame.mixer.music.stop()
    return "stop basarili"


@app.route("/pause", methods=['POST'])
def pause():
    pygame.mixer.music.pause()
    return "pause basarili"


@app.route("/unPause", methods=['POST'])
def un_pause():
    pygame.mixer.music.unpause()
    return "unpause basarili"


@app.route("/volumeUp", methods=['POST'])
def volume_up():
    pygame.mixer.music.set_volume(1)
    return "ses yukseltme basarili"


@app.route("/volumeDown", methods=['POST'])
def volume_down():
    pygame.mixer.music.set_volume(0.1)
    return "ses dusurme basarili"


if __name__ == "__main__":
    app.run(debug=True)
