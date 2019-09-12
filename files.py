import json
import mido
from playsound import playsound


with open("melodyWater.json", "r") as song_json:
    melo_json = json.load(song_json)

mid = mido.MidiFile('Melody of Water_Tales of Zestiria.mid')
i = 0
melo_name = melo_json["header"]["name"]
melo_bpm = melo_json["header"]["bpm"]
melo_duration = melo_json["duration"]
#print(melo_note)



for msg in mid.play():
    melo_note = melo_json["tracks"][1]["notes"][i]["name"]
    playsound("./mp3 Notes/" + melo_note + ".mp3")
    i = i + 1
    print(melo_note)

#for p in melo_note:
    #print(p)


class Song:

    def __init__(self, name, duration, bpm):
        self.name = name
        self.duration = duration
        self.bpm = bpm


melody = Song(melo_name, melo_duration, melo_bpm)