from tkcalendar import *
import Playlist
import tkinter as tk


class Phase5:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Event Planner!')
        self.root.geometry("600x400")
        self.cal1 = Calendar(self.root, selectmode="day", year=2022, month=11, day=17, foreground='red',
                             headersbackground='black')
        self.cal1.pack(pady=20)
        self.label1 = tk.Label(self.root, text="")
        button1 = tk.Button(self.root, text="Set Event Date", command=self.get_date)
        button1.pack(pady=20)
        button2 = tk.Button(self.root, text="Create Event", command=self.create_event)
        button2.pack(pady=20)
        self.label1.pack(pady=20)

        self.root.mainloop()

    def get_date(self):
        self.label1.config(text=self.cal1.get_date())

    def create_event(self):
        # Date of event
        Event_Date = self.cal1.get_date()
        # Name of event
        Event_Name = input("What do you want your event to be called?: ")
        # Event Start Time
        Start_Time = input("What time will your event start (Example: 7:00AM or 7AM): ")
        # Event end time
        End_time = input("What time will your event end? (Example: 8:00PM or 8PM): ")
        print()
        newplaylist = Playlist.Playlist()
        newplaylist.PrintPlaylist('Playlist for: ' + Event_Name + ' on ' + Event_Date + ' from [' + Start_Time
                                  + '-' + End_time + ']',Event_Name)
