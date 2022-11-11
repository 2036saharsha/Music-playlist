import calendar
import Playlist

class MakeEvent:
    yy = 2022
    mm = 11
    Event_List_Index = 0
    Events_List = [None]
    my_events = {}

    def __init__(self):
        Event_Date = input("What day is your event on? (Please enter in mm/dd/yyyy format): ")
        self.mm = int(Event_Date[0:2])
        self.yy = int(Event_Date[6:10])
        self.PrintCalendar()
        print()
        # Name of event
        Event_Name = input("What do you want your event to be called?: ")
        # Event Start Time
        Start_Time = input("What time will your event start (Example: 7:00AM or 7AM): ")
        # Event end time
        End_time = input("What time will your event end? (Example: 8:00PM or 8PM): ")
        self.Events_List[self.Event_List_Index] = (list[Event_Date, Start_Time, End_time])
        self.Event_List_Index += 1
        self.my_events.update({Event_Name: Event_Date})
        temp = list((self.my_events.keys()))
        print()
        print()
        print("Lets get you some music for " + temp[0] + " on " + self.my_events.get(Event_Name))
        print()
        newplaylist = Playlist.Playlist(Event_Name)
        newplaylist.PrintPlaylist()

    def PrintCalendar(self):
        print(calendar.month(self.yy, self.mm))
