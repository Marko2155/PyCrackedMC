import subprocess

from textual.app import *
from textual.widgets import *
from textual.containers import *
from textual.screen import *
from minecraft_launcher_lib import *
import webbrowser
import random
import subprocess
import os

path = os.getcwd()

minecraft_directory = utils.get_minecraft_directory()
minecraft_version = utils.get_latest_version()["release"]

options = {
    "username": "PCMPlayer" + str(random.randrange(0, 10000)),
    "uuid": "30c807a0-7d6d-44cf-960b-a7e8c1bafc7c",
    "token": "pineapple-pizza"
}


class LoginPanel(Screen):

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "settings":
            app.pop_screen()
            app.push_screen("settings")
        elif event.button.id == "play":
            if os.path.exists(path + "username"):
                options["username"] = open(path + "username", "rt").read()
            else:
                with open(path + "username", "x") as unameFile:
                    unameFile.write(options["username"])
                    unameFile.close()
            install.install_minecraft_version(minecraft_version, minecraft_directory)
            minecraft_command = command.get_minecraft_command(minecraft_version, minecraft_directory, options)
            if os.path.exists(path + "mc.log"):
                os.remove(path + "mc.log")
                logfile = open(path + "mc.log", "x")
            else:
                logfile = open(path + "mc.log", "x")
            subprocess.run(minecraft_command, stdout=logfile)

    def compose(self) -> ComposeResult:
        yield Label("Version: " + str(minecraft_version))
        yield Button("Play", id="play", variant="success")
        yield Button("Settings", id="settings")


class SettingsPanel(Screen):

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "settings_back":
            app.pop_screen()
            app.push_screen("login")
        elif event.button.id == "open-minecraft-dir":
            webbrowser.open('file:///' + minecraft_directory)
        elif event.button.id == "change-username":
            subprocess.run([sys.executable, path + "changeUsername.py"])

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Button("Open .minecraft directory", id="open-minecraft-dir")
        yield Button("Change username", id="change-username", variant="success")
        yield Button("Back", variant="error", id="settings_back")


class PyCrackMC(App):
    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode"), ("q", "quit", "Quit")]
    SCREENS = {
        "login": LoginPanel(),
        "settings": SettingsPanel()
    }

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def action_quit(self) -> None:
        exit(0)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        app.push_screen("login")


if __name__ == "__main__":
    if path.endswith("assets"):
        path = "./"
    else:
        path = "assets/"
    app = PyCrackMC()
    app.run()
