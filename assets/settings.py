import tkinter as tk
import subprocess
import os
import sys
from minecraft_launcher_lib import utils
import webbrowser

path = os.getcwd()
if path.endswith("assets"):
    path = "./"
else:
    path = "assets/"

minecraft_directory = utils.get_minecraft_directory()

def openUser():
    subprocess.run([sys.executable, path + "changeUsername.py"])

def exitProg():
    root.destroy()

def openMinecraftDir():
    webbrowser.open('file:///' + minecraft_directory)

def openVersion():
    subprocess.run([sys.executable, path + "changeVersion.py"])

root = tk.Tk()
root.title("Settings")
root.geometry("250x150")
root.resizable(False, False)
openminecraftdir = tk.Button(root, text="Open .minecraft directory", command=openMinecraftDir)
openminecraftdir.pack()
changeusername_button = tk.Button(root, text="Change username", command=openUser)
changeusername_button.pack()
changeversion_button = tk.Button(root, text="Change version", command=openVersion)
changeversion_button.pack()
back_button = tk.Button(root, text="Back", command=exitProg)
back_button.pack()

root.mainloop()
