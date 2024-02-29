import tkinter as tk
import os

path = os.getcwd()

if path.endswith("assets"):
    path = "./"
else:
    path = "assets/"


def setVersion():
    if os.path.exists(path + "version"):
        os.remove(path + "version")
    with open(path + "version", "x") as f:
        f.write(str(version.get()))
        f.close()
    root.destroy()

def useLatest():
    if os.path.exists(path + "version"):
        os.remove(path + "version")
    root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Change Version")
    root.resizable(False, False)
    root.geometry("250x150")

    version_var = tk.StringVar()
    version = tk.Entry(root, textvariable=version_var)
    version.pack()

    if os.path.exists(path + "version"):
        version_var.set(open(path + "version").read())

    ok = tk.Button(root, text="Ok", command=setVersion)
    ok.pack()

    useDefault = tk.Button(root, text="Use Latest", command=useLatest)
    useDefault.pack()

    back = tk.Button(root, text="Back", command=root.quit)
    back.pack()

    root.mainloop()
