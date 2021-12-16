from tkinter import *
import tkinter as tk
import json


class AtmApplication:
    def __init__(self, screen=False):
        # Fullscreen Disable [false] at default
        self. window = tk.Tk()
        self.screen = screen

    def getAuthentication(self) -> None: pass
    def bindKeyboardEvent(self) -> None: pass

    def getApplicationName(self):
        application_file = open("manifest.json")
        application_name = json.load(application_file)
        return application_name["application"]["name"]

    def getUserData(self, key="name"):
        dummy_user = open('data/user.json')
        dummy_data = json.load(dummy_user)
        return dummy_data[key]

    def bindWindowConfiguration(self):
        self.window.title(self.getApplicationName())
        self.window.iconbitmap("assets/images/atm.ico")
        self.window.configure(bg="blue")
        self.window.geometry("1000x500")
        self.window.state('zoomed')
        self.window.attributes("-fullscreen", False)
        self.window.mainloop()


if __name__ == "__main__":
    application = AtmApplication(screen=False)
    application.bindWindowConfiguration()
