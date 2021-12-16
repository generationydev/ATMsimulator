from tkinter import *
import tkinter as tk
import sys


class DepositPage():
    def __init__(self, screen):
        self.title = "Deposit Page"
        self.screen = screen
        self.window = tk.Tk()

    def main(self): pass

    def bindWindowConfiguration(self):
        self.window.title(self.title)
        self.window.iconbitmap("assets/images/atm.ico")
        self.window.configure(bg="#00008b")
        self.window.geometry("1000x500")
        self.window.state('zoomed')
        self.window.attributes("-fullscreen", self.screen)
        self.window.mainloop()
