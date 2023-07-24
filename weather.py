import requests
import PySimpleGUI as Sg
req = requests.get("https://data.buienradar.nl/2.0/feed/json")
data = req.json()
print(data)
print(data['actual']['stationmeasurements'][23]['temperature'])
temp = data['actual']['stationmeasurements'][23]['temperature'], 'C'
print(temp)

text = (None, 20)

layout = [[Sg.Text("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii weather stats!", size=(40, 1), font=text),
           [Sg.Text(temp, font=text)]]]

window = Sg.Window('test!', layout, margins=(100, 50))

while True:
    event, values = window.read()
    if event == Sg.WIN_CLOSED:
        break

window.close()
