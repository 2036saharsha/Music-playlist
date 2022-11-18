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
        
        tk.mainloop()

    def get_date(self):
        self.label1.config(text=self.cal1.get_date())

    def start_playlist(self, edate, ename, stime, etime):
        newplaylist = Playlist.Playlist()
        newplaylist.PrintPlaylist('Playlist for: ' + ename + ' on ' + edate + ' from [' + stime
                                  + '-' + etime + ']', ename)

    def create_event(self):
        
        self.top = tk.Toplevel(self.root)
        self.top.title('Creating Event')
        self.top.geometry("600x400")
        
        Event_Date = self.cal1.get_date()
        Event_Name = tk.StringVar()
        Start_Time = tk.StringVar()
        End_Time = tk.StringVar()
        
        # testing labels
        #label = tk.Label(self.top, text = "This is the second window").pack()
        
        # creating a label for
        # name using widget Label
        name_label = tk.Label(self.top, text = "What do you want your event to be called?: ").pack()
        name_entry = tk.Entry(self.top, textvariable = Event_Name, font = ('calibre',10,'normal')).pack()
        
        start_label = tk.Label(self.top, text = "What time will your event start (Example: 7:00AM or 7AM): ").pack()
        start_entry = tk.Entry(self.top, textvariable = Start_Time, font = ('calibre',10,'normal')).pack()
        
        end_label = tk.Label(self.top, text = "What time will your event end? (Example: 8:00PM or 8PM): ").pack()
        end_entry = tk.Entry(self.top, textvariable = End_Time, font = ('calibre',10,'normal')).pack()
        
        # creating a button using the widget
        # Button that will call the submit function
        sub_btn = tk.Button(self.top, text = "Submit", command = lambda: self.start_playlist(str(Event_Date), str(Event_Name), str(Start_Time), str(End_Time)))
        sub_btn.pack()
        
        # placing the label and entry in
        # the required position using grid
        # method
        #name_label.grid(row=0,column=0)
        #name_entry.grid(row=0,column=1)
        #start_label.grid(row=1,column=0)
        #start_entry.grid(row=1,column=1)
        #end_label.grid(row=2,column=0)
        #end_entry.grid(row=2,column=1)
        #sub_btn.grid(row=3,column=1)

        # Date of event
        #Event_Date = self.cal1.get_date()
        # Name of event
        #Event_Name = input("What do you want your event to be called?: ")
        # Event Start Time
        #Start_Time = input("What time will your event start (Example: 7:00AM or 7AM): ")
        # Event end time
        #End_Time = input("What time will your event end? (Example: 8:00PM or 8PM): ")
        