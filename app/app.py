import eyed3
from flask import Flask, render_template, request
import pygame
import os
from flask import request

app = Flask(__name__)

songs_path = "/home/burcin/song/"
music = "/home/burcin/song/01.TheCrushOfLove.mp3"
pygame.init()

pygame.mixer.music.load(music)
song_info_list = []


@app.route("/")
def song_information():
    songs = os.listdir(songs_path)
    for song in songs:
        if song.endswith(".mp3"):
            path = songs_path + song
            audiofile = eyed3.load(path)
            song_info = {'artist': audiofile.tag.artist, 'album': audiofile.tag.artist, 'title': audiofile.tag.title,
                         'genre': audiofile.tag.genre, 'path': path}
            song_info_list.append(song_info)
    return render_template('index.html', song_info_list = song_info_list)


@app.route("/play", methods=['GET','POST'])
def play():
    # path1 = request.form['path']
    # print(path1)
    #import pdb
    #pdb.set_trace()
    #music1 = "/home/burcin/song" + title
    #print(music1)
    # pygame.mixer.music.load(path1)
    pygame.init()
    pygame.mixer.music.play()
    return 'basarili'


@app.route("/stop", methods=['POST'])
def stop():
    pygame.mixer.music.stop()
    return "stop basarili"


if __name__ == "__main__":
    app.run()
