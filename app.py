from tkinter import *
import tkinter as tk
import json


class AtmApplication:
    def __init__(self) -> None: pass
    window = tk.Tk()

    def getAuthentication(self): pass

    def getApplicationName(self):
        application_file = open("manifest.json")
        application_name = json.load(application_file)
        return application_name["application"]["name"]

    def getUserData(self, key="name"):
        dummy_user = open('data/user.json')
        dummy_data = json.load(dummy_user)
        return dummy_data[key]

    if __name__ == "__main__":
        window.title(getApplicationName(self=None))
        window.iconbitmap("assets/images/atm.ico")
        window.geometry("1000x500")
        window.mainloop()
