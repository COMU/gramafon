import eyed3
from flask import Flask, render_template, request
import pygame
import os
import json
from flask import jsonify

# from flask.ext.triangle import Triangle

app = Flask(__name__)

songs_path = "/home/burcin/song/"
music = "/home/burcin/song/01.TheCrushOfLove.mp3"
pygame.init()

pygame.mixer.music.load(music)



@app.route("/")
def song_information():
    song_info_list = []
    songs = os.listdir(songs_path)
    for song in songs:
        if song.endswith(".mp3"):
            path = songs_path + song
            audiofile = eyed3.load(path)
            song_info = {'artist': audiofile.tag.artist, 'album': audiofile.tag.artist, 'title': audiofile.tag.title,
                         'path': path}
            song_info_list.append(song_info)
    return render_template("index.html", song_info_list=song_info_list)


@app.route("/play", methods=['POST'])
def play():
    # import ipdb
    # ipdb.set_trace()

    request_body = json.loads(request.get_data())


    song_path=request_body['song']

    pygame.mixer.music.load(song_path)
    pygame.init()
    pygame.mixer.music.play()
    return "basarili"


@app.route("/stop", methods=['POST'])
def stop():
    pygame.mixer.music.stop()
    return "stop basarili"


if __name__ == "__main__":
    app.run(debug=True)
