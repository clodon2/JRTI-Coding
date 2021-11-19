# Corey Verkouteren
# 11/19/21
# Mr Ball's PM
# OOP Practice

# Ski Resort Software

import PySimpleGUI as sg


class guest:
    def __init__(self, Name, Skill, Lessons, Rent, Stay):
        self.Name = Name
        self.Information = [Name, Skill, Lessons, Rent, Stay]


sg.theme("lightblue3")


def window1():
    layout2 = [[sg.Text("Guest Information", s=50, justification="center")],
               [sg.Column([[sg.Text("Name:"),
                            sg.Input(s=30)]],
                          justification="center")],
               [sg.Column([[sg.Text("Skill Level:"),
                            sg.Combo(["Beginner", "Intermediate", "Advanced"], s=10, readonly=True),
                            sg.Text("Length of stay:"),
                            sg.Input(s=3, p=1),
                            sg.Text("days", p=0)]],
                          justification="center")],
               [sg.Column([[sg.Checkbox("Are you renting equipment?"),
                            sg.Checkbox("Do you want lessons?")]],
                          justification="center")],
               [sg.Column([[sg.Button("Submit")]],
                          justification="center")]]

    window2 = sg.Window("Powder Ski Resort", layout2, finalize=True, use_default_focus=False)

    showing2 = True

    while showing2:
        event2, values2 = window2.read()

        if event2 == sg.WINDOW_CLOSED:
            break


layout0 = [[sg.Text("Welcome to Powder Ski Resort!", s=29, font=("Roboto", 20), justification="center",)],
           [sg.Image("skier1Corey.png")],
           [sg.Column([[sg.Button("I am a guest", enable_events=True, k="-guestbutton"),
                        sg.Button("I am a staff member", enable_events=True, k="-staffbutton")]],
                      justification="center")]]


window = sg.Window("Powder Ski Resort", layout0, finalize=True, use_default_focus=False)

showing = True

while showing:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-guestbutton":
        window1()
