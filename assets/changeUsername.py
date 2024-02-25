import tkinter as tk
import tkinter.messagebox as tkm
import os

path = os.getcwd()

if path.endswith("assets"):
    path = "./"
else:
    path = "assets/"

root = tk.Tk()
root.title("Change Username")
root.resizable(False, False)
root.geometry("250x100")
label = tk.Label(root, text="New username:")
label.pack()
entry = tk.Entry(root)
entry.pack()


def changeUsername():
    username = entry.get()
    if os.path.exists(path + "username"):
        os.remove(path + "username")
    if username == "":
        tkm.showerror("Error", "Please enter a username.")
    else:
        with open(path + "username", "x") as usernameFile:
            usernameFile.write(username)
            usernameFile.close()
            root.destroy()


def exitProg():
    exit(0)


cancel = tk.Button(root, text="Cancel", command=exitProg)
ok = tk.Button(root, text="Ok", command=changeUsername)

ok.pack()
cancel.pack()

root.mainloop()
