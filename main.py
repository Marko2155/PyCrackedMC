import os
import sys
import requests as req
import subprocess

launcher_link = "https://raw.githubusercontent.com/Marko2155/PyCrackedMC/main/assets/launcher.py"
launcher_name = "launcher.py"
original_textual = False

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def create_run_launcher():
    if os.path.exists("./assets/launcher.py"):
        print("Reinstalling " + launcher_name)
        os.remove("./assets/launcher.py")
    if os.path.exists("assets/changeUsername.py"):
        print("Reinstalling changeUsername.py")
        os.remove("assets/changeUsername.py")
    url1 = launcher_link
    res1 = req.get(url1)
    launcherCode = res1.text
    url2 = "https://raw.githubusercontent.com/Marko2155/PyCrackedMC/main/assets/changeUsername.py"
    res2 = req.get(url2)
    changeUsernameCode = res2.text
    if original_textual is False:
        if os.path.exists("assets/settings.py"):
            print("Reinstalling settings.py")
            os.remove("assets/settings.py")
        url3 = "https://raw.githubusercontent.com/Marko2155/PyCrackedMC/main/assets/settings.py"
        res3 = req.get(url3)
        settingsCode = res3.text
        with open("assets/settings.py", "x") as f:
            f.write(settingsCode)
            f.close()
    with open("./assets/launcher.py", "x") as f:
        f.write(launcherCode)
        f.close()
    with open("assets/changeUsername.py", "x") as f:
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

if len(sys.argv) > 1:
    if sys.argv[1] == "--textual":
        original_textual = True
        launcher_link = "https://raw.githubusercontent.com/Marko2155/PyCrackedMC/main/assets/launcher.bak.py"
        launcher_name = "the original launcher.py"
    else:
        print("main.py: Unrecognized argument")
        exit(0)

if os.path.exists("./assets"):
    create_run_launcher()
else:
    os.mkdir("./assets")
    create_run_launcher()
