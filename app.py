import importlib.util
import json
import sys
import os
from tkinter import *
import tkinter as tk
from database.database import Database
from components.theme import ComponentColours


class AtmApplication:
    def __init__(self, bank_name, screen=False):
        self. window = tk.Tk()
        self.bank_name = bank_name
        self.screen = screen

    def main(self):
        self.getModules()
        self.bindKeyboardEvent()
        self.renderUserComponents()
        self.bindWindowConfiguration()

    def getAuthentication(self) -> None: pass

    def getModules(self):
        sys.path.insert(0, "database/")
        package_tkinter = importlib.util.find_spec('tkinter')

        if package_tkinter is None:
            try:
                os.system("pip install tk")
            except:
                raise Exception("Please install Tkinter Manually")
        else:
            pass

    def bindKeyboardEvent(self):
        self.window.bind(
            "<F11>", lambda event: self.window.attributes("-fullscreen", True)
        )
        self.window.bind(
            "<F10>", lambda event: self.window.attributes("-fullscreen", False)
        )

    def getApplicationName(self):
        application_file = open("manifest.json")
        application_name = json.load(application_file)
        return application_name["application"]["name"]

    def getManifestationItem(self, key1, key2):
        application_file = open("manifest.json")
        application_manifestation = json.load(application_file)
        return application_manifestation[key1][key2]

    def getUserData(self, key="name"):
        dummy_user = open('data/user.json')
        dummy_data = json.load(dummy_user)
        return dummy_data[key]

    def renderUserComponents(self):
        welcome_message = Label(
            self.window,
            foreground=ComponentColours.yellow(),
            bg=ComponentColours.blue(),
            text=f"WELCOME TO {self.bank_name.upper()}BANK",
            font=("Arial-Black 25")
        )

        screen_deposit = Label(
            self.window,
            foreground=ComponentColours.yellow(),
            bg=ComponentColours.blue(),
            text=self.getManifestationItem(
                key1="labels", key2="0"
            ),
            font=("Arial-Black 25")
        )

        screen_transfer = Label(
            self.window,
            foreground=ComponentColours.yellow(),
            bg=ComponentColours.blue(),
            text=self.getManifestationItem(
                key1="labels", key2="4"
            ),
            font=("Arial-Black 25")
        )

        screen_withdrawal = Label(
            self.window,
            foreground=ComponentColours.yellow(),
            bg=ComponentColours.blue(),
            text=self.getManifestationItem(
                key1="labels", key2="1"
            ),
            font=("Arial-Black 25")
        )

        screen_paybills = Label(
            self.window,
            foreground=ComponentColours.yellow(),
            bg=ComponentColours.blue(),
            text=self.getManifestationItem(
                key1="labels", key2="2"
            ),
            font=("Arial-Black 25")
        )

        welcome_message.pack(side="bottom")
        screen_deposit.place(relx=0.10, rely=0.2, anchor="w")
        screen_deposit.bind(
            "<Button-1>", lambda event: self.navigate('deposit')
        )
        screen_transfer.place(relx=0.10, rely=0.4, anchor="w")
        screen_transfer.bind("<Button-1>", lambda event: print("Transfer"))
        screen_withdrawal.place(relx=0.65, rely=0.2, anchor="w")
        screen_withdrawal.bind("<Button-1>", lambda event: print("withdrawal"))
        screen_paybills.place(relx=0.70, rely=0.4, anchor="w")
        screen_paybills.bind("<Button-1>", lambda event: print("paybills"))

    def navigate(self, className):
        if className is None:
            return "Class Name Invalid"
        if className == "deposit":
            self.onExit
            from pages.deposit import DepositPage
            DepositPage(screen=self.screen)

    def bindWindowConfiguration(self):
        self.window.title(self.getApplicationName())
        self.window.iconbitmap("assets/images/atm.ico")
        self.window.configure(bg="#00008b")
        self.window.geometry("1000x500")
        self.window.state('zoomed')
        self.window.attributes("-fullscreen", self.screen)
        self.window.mainloop()

    def onExit(self):
        self.window.destroy()


if __name__ == "__main__":
    application = AtmApplication(bank_name="may", screen=False)
    application.main()
