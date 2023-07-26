import requests
import PySimpleGUI as sg
import time
#from flask import Flask
import subprocess
import PySimpleGUIWeb

# a small project to display different information selected via a webui ment for a raspberry pi with only a screen
# also ment to easily add more .py files
# currently not ready

print("Hello world")

yes = 0

CurrentApp = 0 # 0 = nothing 1 is weather 2 is chess
Selected = 0

while yes == 0: # This should be on always
    CurrentApp = int(input("select ")) # temp will be replaced by a webapp maybe pysimpleweb?
    if Selected == 0: # This is used to terminate the other module if a new one is selected
        print("0")
    elif Selected == 1 and CurrentApp != 1:
        weather.terminate()
        Selected = 0
    elif Selected == 2 and CurrentApp !=2:
        chess.terminate()
        gui.terminate()
        Selected = 0

    if CurrentApp == 1 and Selected != 1: # Selected != is to prevent the app from opening twice
        weather = subprocess.Popen(["python", "weather.py"])
        Selected = 1
        time.sleep(2)
    elif CurrentApp == 2 and Selected != 2:
        chess = subprocess.Popen(["python", "ches.py"])
        time.sleep(1)
        gui = subprocess.Popen(["python", "chessgui.py"])
        Selected = 2
        time.sleep(2)