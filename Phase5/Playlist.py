import requests
from tkinter import *


class Playlist:
    response = list()

    def __init__(self):
        artist1 = input("Name of the first artist you would like to hear: ")
        song1 = input("Name of a song by said artist, similar to what you'd like to hear: ")
        artist2 = input("Name of the second artist you'd like to hear: ")
        song2 = input("Name of a song by said artist: ")
        artist3 = input("Name of 3rd artist you'd want to hear: ")
        song3 = input("Name of a song you'd want to hear: ")
        print()

        url = "https://spotify-tracks.p.rapidapi.com/"
        payload = {
            "tracks": {
                artist1: song1,
                artist2: song2,
                artist3: song3
            },
            "n": 20
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "557be65fb1mshe48ec2d568154e4p1eca67jsn636e2088244d",
            "X-RapidAPI-Host": "spotify-tracks.p.rapidapi.com"
        }
        self.response = requests.request("POST", url, json=payload, headers=headers)

    def PrintPlaylist(self, title):
        root = Tk()
        root.title(title)
        root.geometry("300x200")
        w = Label(root, text=self.response.text.replace(',', '\n'), font="50")
        print(self.response.text.replace(',', '\n'))
        print('-------------------------------------------------')
        w.pack()
        root.mainloop()



