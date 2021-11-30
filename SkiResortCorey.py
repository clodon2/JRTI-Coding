# Corey Verkouteren
# 11/19/21
# Mr Ball's PM
# OOP Practice

# Ski Resort Software

import PySimpleGUI as sg


class guest:
    def __init__(self, Name, Skill, Lessons, Rent, Stay):
        self.Information = [Name, Skill, Stay, Lessons, Rent]

    def getName(self):
        return self.Information[0]

    def getInformation(self):
        return self.Information

    def getSkill(self):
        return self.Information[1]

    def getLessons(self):
        return self.Information[3]

    def getRent(self):
        return self.Information[4]

    def getStay(self):
        return self.Information[2]


sg.theme("lightblue3")


def createwindow2():
    layout2 = [[sg.Text("Guest Information", font=("Roboto", 15), justification="center", s=40)],
               [sg.Column([[sg.Text("Name:"),
                            sg.Input(s=30, k="-guestname")]],
                          justification="center")],
               [sg.Column([[sg.Text("Skill Level:"),
                            sg.Combo(["Beginner", "Intermediate", "Advanced"], s=10, readonly=True, k="-guestskill"),
                            sg.Text("Length of stay:"),
                            sg.Input(s=3, p=1, k="-gueststay"),
                            sg.Text("days", p=0)]],
                          justification="center")],
               [sg.Column([[sg.Checkbox("Are you renting equipment?", k="-guestrent"),
                            sg.Checkbox("Do you want lessons?", k="-guestlesson")]],
                          justification="center")],
               [sg.Column([[sg.Button("Submit", k="-guestsubmit", enable_events=True)]],
                          justification="center")]]

    window2 = sg.Window("Powder Ski Resort Guest Sign-In", layout2, finalize=True, use_default_focus=False)
    window2.make_modal()

    showing2 = True

    while showing2:
        event2, values2 = window2.read()

        if event2 == sg.WINDOW_CLOSED:
            break

        if event2 == "-guestsubmit":

            if window2["-guestname"].get() == "" or window2["-guestskill"].get() == "":
                sg.popup_ok_cancel("Please fill in all fields")

            elif not window2["-gueststay"].get().isdigit():
                sg.popup_ok_cancel("Please only use integers when selecting your stay time")

            else:
                user = window2["-guestname"].get()

                if user in guestlist:
                    sg.popup_ok_cancel("Guest already booked")

                else:
                    guestlist.append(user)
                    user = guest(window2["-guestname"].get(), window2["-guestskill"].get(), window2["-guestlesson"].get(),
                              window2["-guestrent"].get(), window2["-gueststay"].get())
                    guesttableinfo.append(user.getInformation())


def createwindow3():
    layout3 = [[sg.Frame("Guest Index", font=("Roboto", 15), layout=
                         [[sg.Table(values=guesttableinfo,
                                    headings=["Guest Name", "Skill Level", "Days Staying", "Renting Equipment", "Wants Lessons"],
                                    visible_column_map=[True, True, True, True, True], def_col_width=25,
                                    justification="left")]],
                         title_location="n")]]

    window3 = sg.Window("Powder Ski Resort Guest Information", layout3, finalize=True, use_default_focus=False)
    window3.keep_on_top_set()

    showing3 = True

    while showing3:
        event3, values3 = window3.read()

        if event3 == sg.WINDOW_CLOSED:
            break


layout0 = [[sg.Text("Welcome to Powder Ski Resort!", s=29, font=("Roboto", 20), justification="center",)],
           [sg.Image("skier1Corey.png")],
           [sg.Column([[sg.Button("I am a guest", enable_events=True, k="-guestbutton"),
                        sg.Button("I am a staff member", enable_events=True, k="-staffbutton")]],
                      justification="center")]]


window = sg.Window("Powder Ski Resort", layout0, finalize=True, use_default_focus=False)

guestlist = []
guesttableinfo = []

showing = True

while showing:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-guestbutton":
        createwindow2()

    if event == "-staffbutton":
        print(guesttableinfo)
        createwindow3()
