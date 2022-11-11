import pywhatkit
import time
class Music_Player:
    def __init__(self,songs):
        self.songs=songs
    def play_song(self):
        songs=self.songs
        for song in songs:
            try:
                pywhatkit.playonyt(song)
                print("Playing...",song)
                time.sleep(300)
            except:
               # printing the error message
                print("Network Error Occurred") 
                exit()
        
                        
        
