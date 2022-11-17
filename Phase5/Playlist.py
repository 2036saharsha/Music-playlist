import requests
import Music_Player
import tkinter as tk
import time
from threading import Thread
class Playlist:
    response = list()
    def __init__(self):
        artist1 = input("Name of the first artist you would like to hear: ")
        song1 = input("Name of a song by said artist, similar to what you'd like to hear: ")
        artist2 = input("Name of the second artist you'd like to hear: ")
        song2 = input("Name of a song by said artist: ")
        print()

        url = "https://spotify-tracks.p.rapidapi.com/"
        payload = {
            "tracks": {
                artist1:song1,
                artist2: song2,
                
            },
            "n": 20
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "557be65fb1mshe48ec2d568154e4p1eca67jsn636e2088244d",
            "X-RapidAPI-Host": "spotify-tracks.p.rapidapi.com"
        }
        self.response = requests.request("POST", url, json=payload, headers=headers)
    def filter_data(self):
        data=self.response.text
        data=str(data)
        data=data.replace("[","")
        data=data.replace("]","")
        data=data.replace('"',"")
        res=data.split(',')
        songs=[]
        for val in res:
            songs.append(val)
        return songs

    def PrintPlaylist(self,title,eventName):

        songs=Playlist.filter_data(self)
        self.root = tk.Tk()
        self.root.title("Music_System")
        self.root.geometry("1280x900")
        img=tk.PhotoImage(master=self.root,file="Music.png")
        tk.Label(self.root,image=img).pack(side=tk.LEFT)

        play_button=tk.PhotoImage(master=self.root,file = "play.png")
        button1 = tk.Button(master=self.root, text="Play Song",image=play_button,bg='blue',command=self.PlaySong)
        button1.place(x=310,y=550)
        x=360
        y=560
        for song in songs[:5]:
            playlist = tk.Label(self.root, text=song, font=("Times",10),bg="white",fg="black").place(x=x,y=y)
            y+=50
            # playlist.pack()
        print("Songs added to the playlist")
        print()
        for song in songs:
            print(song)
        print('-------------------------------------------------')
        self.database(songs,eventName)
        # songs_playing.pack()
        
        # p1=Thread(target=self.PlaySong(songs))
        # p2=Thread(target=self.root.mainloop())
        # p1.start()
        # p2.start
        
        self.root.mainloop()
    def database(self,songs,eventName):
        f = open("database.txt", "a")
        f.write(f'{eventName} = {str(set(songs))}\n')
        f.close()
    def PlaySong(self):
        songs=self.filter_data()
        player=Music_Player.Music_Player(songs)
        player.play_song()






