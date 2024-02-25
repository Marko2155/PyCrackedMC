import os
import sys
import requests as req
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def create_run_launcher():
    if os.path.exists("./assets/launcher.py"):
        print("Reinstalling launcher.py")
        os.remove("./assets/launcher.py")
    if os.path.exists("./assets/changeUsername.py"):
        print("Reinstalling changeUsername.py")
        os.remove("./assets/changeUsername.py")
    url1 = "https://raw.githubusercontent.com/Marko2155/PyCrackedMC/main/assets/launcher.py"
    res1 = req.get(url1)
    launcherCode = res1.text
    url2 = "https://raw.githubusercontent.com/Marko2155/PyCrackedMC/main/assets/changeUsername.py"
    res2 = req.get(url2)
    changeUsernameCode = res2.text
    with open("./assets/launcher.py", "x") as f:
        f.write(launcherCode)
        f.close()
    with open("./assets/changeUsername.py", "x") as f:
        f.write(changeUsernameCode)
        f.close()
    print("Finished")
    subprocess.run([sys.executable, "./assets/launcher.py"])

try:
    import textual
except ImportError:
    print("[INFO] Could not find library 'textual' on system, installing")
    install("textual")

try:
    import minecraft_launcher_lib
except ImportError:
    print("[INFO] Could not find library 'minecraft_launcher_lib' on system, installing")
    install("minecraft_launcher_lib")

if os.path.exists("./assets"):
    create_run_launcher()
else:
    os.mkdir("./assets")
    create_run_launcher()
