#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import requests
import time

req = requests.get("https://data.buienradar.nl/2.0/feed/json")
data = req.json()
print(data)
print(data['actual']['stationmeasurements'][19]['temperature'])
temp = data['actual']['stationmeasurements'][19]['temperature']
cur = data['actual']['stationmeasurements'][19]['weatherdescription']
times = data['actual']['stationmeasurements'][19]['timestamp']
icon = data['actual']['stationmeasurements'][19]['iconurl']
requests.get(icon)
# Get all the weather data into variables
## filename = "icon_image.jpg"

## with open(filename, 'wb') as f:
##     f.write(requests.get(icon).content)
# Unused but this is for downloading the current weather icon
print(temp)
print(cur)
print(times)
print(icon)

#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

# ui i made with pygubu-designer <3
class Weather3App:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.overrideredirect(True)
        toplevel1.configure(height=480, width=480)


        screen_width = toplevel1.winfo_screenwidth()
        screen_height = toplevel1.winfo_screenheight()
        x_position = (screen_width - 480) // 2
        y_position = (screen_height - 480) // 2
        toplevel1.geometry(f"480x480+{x_position}+{y_position}")


        label1 = ttk.Label(toplevel1)
        self.img_sc = tk.PhotoImage(file="sc.png")
        label1.configure(borderwidth=0, image=self.img_sc, text='label1')
        label1.grid(column=0, row=0)
        label2 = ttk.Label(toplevel1)
        label2.configure(
            background="#000000",
            font="{Noto Sans} 36 {}",
            foreground="#fff",
            text=temp)
        label2.place(anchor="nw", relx=0.0, x=100, y=150)
        label3 = ttk.Label(toplevel1)
        label3.configure(
            background="#000000",
            font="{Noto Sans} 20 {}",
            foreground="#fff",
            text='C°')
        label3.place(anchor="nw", relx=0.0, x=200, y=150)
        label4 = ttk.Label(toplevel1)
        label4.configure(
            background="#000000",
            font="{Noto Sans} 24 {}",
            foreground="#fff",
            text=times)
        label4.place(anchor="nw", relx=0.0, x=50, y=50)
        label5 = ttk.Label(toplevel1)
        label5.configure(
            background="#000000",
            font="{Noto Sans} 15 {}",
            foreground="#fff",
            text=cur)
        label5.place(anchor="nw", relx=0.0, x=50, y=400)

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = Weather3App()
    app.run()
