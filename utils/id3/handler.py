#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chardet
from mutagen import mp3
from mutagen import flac
from mutagen import ogg



def stripnulls(data):
    "strip whitespace and nulls"
    return data.replace("\00", "").strip()

class MP3FileInfo:
    "store ID3v1.0 MP3 tags"
    tagDataMap = {"title"   : (  3,  33, stripnulls),
                  "singer"  : ( 33,  63, stripnulls),
                  "album"   : ( 63,  93, stripnulls),
                  "year"    : ( 93,  97, stripnulls),
                  "comment" : ( 97, 126, stripnulls),
                  "genre"   : (127, 128, ord)}

    info = dict()

    def parse(self, filename):
        "parse ID3v1.0 tags from MP3 file"
        #self.clear()
        try:
            fsock = open(filename, "rb", 0)
            try:
                fsock.seek(-128, 2)
                tagdata = fsock.read(128)
            finally:
                fsock.close()
            if tagdata[:3] == "TAG":
                for tag, (start, end, parseFunc) in self.tagDataMap.items():
                    self.info[tag] = parseFunc(tagdata[start:end])
                    if isinstance(self.info[tag], int):
                        continue
                    else:
                        coding = "ascii"
                        info = chardet.detect(self.info[tag])
                        if info["confidence"] == 0.99: # kodlaması bu yüzde ile bulunulanlarda sorun var
                            continue
                        if info["confidence"] > 0.5: # içinde Türkçe karakter geçen isimler için alınan verinin utf-8
                        # kodlanması sağlandı
                            coding = info["encoding"]
                            self.info[tag] = self.info[tag].decode(coding).encode("utf-8")
        except IOError:
            pass

    def get_singer_info(self):
        return self.info['singer']

    def get_album_name(self):
        return self.info['album']

    def get_album_date(self):
        return self.info['year']

    def get_song_title(self):
        return self.info['title']
    def get_album2_name(self):
        return self.info['name']

