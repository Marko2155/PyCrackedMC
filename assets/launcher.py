import tkinter as tk
from minecraft_launcher_lib import *
import tkinter.messagebox as tkm
import random
import subprocess
import os
import sys

# New Tkinter Launcher


minecraft_directory = utils.get_minecraft_directory()
path = os.getcwd()
options = {
    "username": "PCMPlayer" + str(random.randrange(0, 10000)),
    "uuid": "a96235c5-9da2-436f-a45d-c38dc84ad28f",
    "token": "pineapple-pizza"
}

if path.endswith("assets"):
    path = "./"
else:
    path = "assets/"

if os.path.exists(path + "version"):
    minecraft_version = open(path + "version").read()
else:
    minecraft_version = utils.get_latest_version()["release"]


if os.path.exists(path + "username"):
    options["username"] = open(path + "username", "rt").read()
else:
    with open(path + "username", "x") as unameFile:
        unameFile.write(options["username"])
        unameFile.close()


def launch_minecraft():
    install.install_minecraft_version(minecraft_version, minecraft_directory)
    minecraft_command = command.get_minecraft_command(minecraft_version, minecraft_directory, options)
    subprocess.run(minecraft_command)


def openSettings():
    p1 = subprocess.Popen([sys.executable, path + "settings.py"])
    p1.wait()
    tkm.showinfo("Information", "Restarting PyCraft Launcher so the changes can take effect")
    subprocess.Popen([sys.executable, path + "launcher.py"])
    exit(0)


root = tk.Tk()
root.title("PyCraft Launcher")
root.geometry("250x100")
version_label = tk.Label(root, text="Version: " + minecraft_version)
version_label.pack()
username_label = tk.Label(root, text="Username: " + options["username"])
username_label.pack()
play_button = tk.Button(root, text="Play", command=launch_minecraft)
play_button.pack()
settings_button = tk.Button(root, text="Settings", command=openSettings)
settings_button.pack()

root.mainloop()
