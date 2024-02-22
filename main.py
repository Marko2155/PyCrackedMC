import os
import sys
import urllib.request
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def create_run_launcher():
    if os.path.exists("./assets/launcher.py"):
        os.remove("./assets/launcher.py")
    with urllib.request.urlopen("https://raw.githubusercontent.com/Marko2155/PyCrackedMC/main/assets/launcher.py") as f:
        launcherCode = f.read().decode("utf-8")
        with open("./assets/launcher.py", "w") as launcherFile:
            launcherFile.write(launcherCode)
            launcherFile.close()
            subprocess.run([sys.executable, "./assets/launcher.py"])

try:
    import textual
except ImportError:
    install("textual")

try:
    import minecraft_launcher_lib
except ImportError:
    install("minecraft_launcher_lib")

if os.path.exists("./assets"):
    create_run_launcher()
else:
    os.mkdir("./assets")
    create_run_launcher()
