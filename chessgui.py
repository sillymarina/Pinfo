import PySimpleGUI as sg

sg.SetOptions(suppress_error_popups=True)

image_path = 'board.png'
layout = [[sg.Image(filename=image_path, pad=(0, 0), key='-IMAGE-')]]
window = sg.Window('Image Display', layout, no_titlebar=True, margins=(0, 0),  finalize=True)

while True:
    event, values = window.read(timeout=100)

    if event == sg.WIN_CLOSED:
        break

    window['-IMAGE-'].update(filename=image_path)

window.close()
