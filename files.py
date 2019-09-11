import json

with open("melodyWater.json", "r") as song_json:
    melo_json = json.load(song_json)

melo_name = melo_json["header"]["name"]
melo_bpm = melo_json["header"]["bpm"]
melo_duration = melo_json["duration"]


#for p in melo_json["tracks"]:
    #print(p["name"])


class Song:

    def __init__(self, name, duration, bpm):
        self.name = name
        self.duration = duration
        self.bpm = bpm


melody = Song(melo_name, melo_duration, melo_bpm)