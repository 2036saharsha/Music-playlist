import requests
import Music_Player
class Playlist:
    response = list()

    def __init__(self,Event_Name):
        artist1 = input("Name of the first artist you would like to hear: ")
        song1 = input("Name of a song by said artist, similar to what you'd like to hear: ")
        artist2 = input("Name of the second artist you'd like to hear: ")
        song2 = input("Name of a song by said artist: ")
        print()
        print(".............Fetching Data For {}............".format(Event_Name))
        url = "https://spotify-tracks.p.rapidapi.com/"
        payload = {
            "tracks": {
                artist1: song1,
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

    def PrintPlaylist(self):
        songs=Playlist.filter_data(self)
        print("Songs added to the playlist: ")
        for song in songs:
            print(song)
        Playlist.PlaySong(self,songs)
    
    def PlaySong(self,songs):
        player=Music_Player.Music_Player(songs)
        player.play_song()





        
        