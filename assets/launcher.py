#!/usr/bin/env python3
import subprocess

from textual.app import *
from textual.widgets import *
from textual.containers import *
from textual.screen import *
from minecraft_launcher_lib import *
import webbrowser

error = ""
uname = ""
path = "assets/"
minecraft_directory = utils.get_minecraft_directory()
minecraft_version = utils.get_latest_version()["release"]

options = {
    "username": "player",
    "uuid": "30c807a0-7d6d-44cf-960b-a7e8c1bafc7c",
    "token": "pineapple-pizza"
}


class ErrorWidget(Static):
    def compose(self) -> ComposeResult:
        yield Label("Error!", id="error-label")
        yield Label(error, id="error-text")


class ErrorPanel(Screen):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Center(ErrorWidget())


class LoginPanel(Screen):

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "settings":
            app.pop_screen()
            app.push_screen("settings")
        elif event.button.id == "play":
            if uname == "":
                options["username"] = "player"
            else:
                options["username"] = uname
            install.install_minecraft_version(minecraft_version, minecraft_directory)
            minecraft_command = command.get_minecraft_command(minecraft_version, minecraft_directory, options)
            if os.path.exists("./assets/mc.log"):
                os.remove("./assets/mc.log")
                logfile = open("./assets/mc.log", "x")
            else:
                logfile = open("./assets/mc.log", "x")
            subprocess.run(minecraft_command, stdout=logfile)

    def compose(self) -> ComposeResult:
        uname = Input(placeholder="Username", type="text", id="username")
        yield uname
        yield Button("Play", id="play", variant="success")
        yield Button("Settings", id="settings")


class SettingsPanel(Screen):

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "settings_back":
            app.pop_screen()
            app.push_screen("login")
        elif event.button.id == "open-minecraft-dir":
            webbrowser.open('file:///' + minecraft_directory)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Button("Open .minecraft directory", id="open-minecraft-dir")
        yield Button("Back", variant="error", id="settings_back")


class PyCrackMC(App):
    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode"), ("q", "quit", "Quit")]
    CSS_PATH = "assets/launcher.tcss"
    SCREENS = {
        "login": LoginPanel(),
        "settings": SettingsPanel(),
        "error": ErrorPanel()
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
    if os.path.exists(path):
        print("[INFO] assets folder exists, continuing")
    else:
        print("[INFO] assets folder does not exist, creating and continuing")
        os.mkdir(path)
    app = PyCrackMC()
    app.run()
