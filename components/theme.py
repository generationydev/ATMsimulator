import json


class ComponentColours:
    def __init__(self, colour):
        self.colour = colour
        self.getColour(name=colour)

    def getColour(self, name):
        switcher = {
            0: 'red',
            1: 'blue',
            2: 'yellow'
        }
        return switcher.get(name, default)

    def red():
        application_manifestation = open("manifest.json")
        application_theme = json.load(application_manifestation)
        return application_theme["ui"]["colours"]["red"]

    def yellow():
        application_manifestation = open("manifest.json")
        application_theme = json.load(application_manifestation)
        return application_theme["ui"]["colours"]["yellow"]

    def blue():
        application_manifestation = open("manifest.json")
        application_theme = json.load(application_manifestation)
        return application_theme["ui"]["colours"]["blue"]

    def default():
        return "Invalid Colour"
