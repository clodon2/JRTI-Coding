# Corey Verkouteren
# 11/19/21 - 12/3/21
# Mr Ball's PM
# OOP Practice

# Ski Resort Software

import PySimpleGUI as sg


class guest:
    def __init__(self, Name, Skill, Lessons, Rent, Stay):
        self.Name = Name
        self.Skill = Skill
        self.Lessons = Lessons
        self.Rent = Rent
        self.Stay = Stay


    def createInformationlist(self):
        gInformation = [self.Name, self.Skill, self.Stay, self.Rent, self.Lessons]
        return gInformation

    def addGuestInformation(self, guesttable, user):
        guesttable.append(user.createInformationlist())


sg.theme("lightblue3")


def tableRowSelection(tabledata, button, skillinfo):
    rownumber = -1
    selectionNumbers = []
    # returns rows to select by counting through the lists in the guesttableinfo list and returning what the count was
    # on if the variable was found (True/False or selected skill level)
    for i in tabledata:
        rownumber += 1
        if button == "lessons":
            if i[4]:
                selectionNumbers.append(rownumber)
        if button == "equipment":
            if i[3]:
                selectionNumbers.append(rownumber)
        if button == "skilllevel":
            if i[1] == skillinfo:
                selectionNumbers.append(rownumber)
    return selectionNumbers


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

            # Prevents fields from being empty or having out of place values like stay time = banana
            if window2["-guestname"].get() == "" or window2["-guestskill"].get() == "":
                sg.popup_ok_cancel("Please fill in all fields")

            elif not window2["-gueststay"].get().isdigit():
                sg.popup_ok_cancel("Please only use integers when selecting your stay time")

            else:
                user = window2["-guestname"].get()

                # prevents repeat guests
                if user in guestlist:
                    sg.popup_ok_cancel("Guest already booked")

                # adds the guest as an object and updates the info for the table in the staff window
                else:
                    guestlist.append(user)
                    user = guest(window2["-guestname"].get(), window2["-guestskill"].get(), window2["-guestlesson"].get(),
                                 window2["-guestrent"].get(), window2["-gueststay"].get())
                    user.addGuestInformation(guesttableinfo, user)
                    sg.popup_ok_cancel("Guest successfully booked")


def createwindow3(tableinfo):
    # prevents an empty table which causes errors
    if not tableinfo:
        tableinfo = [["No Guests Booked", "-", "-", "-", "-"]]

    layout3 = [[sg.Frame("Guest Index", font=("Roboto", 15),
                         layout=[[sg.Table(values=tableinfo,
                                           headings=["Guest Name", "Skill Level", "Days Staying", "Renting Equipment",
                                                     "Wants Lessons"], k="-guesttable",
                                           visible_column_map=[True, True, True, True, True], def_col_width=25, max_col_width=50,
                                           justification="left", selected_row_colors=("White", "skyblue3"))],
                                  [sg.Column([[
                                   sg.Text("Total Guests:"),
                                   sg.Input("0", k="-guesttotal", disabled=True, s=3),
                                   sg.Button("Want Lessons", k="-wantlessons"),
                                   sg.Button("Want Equipment", k="-wantequipment"),
                                   sg.Combo(["Beginner", "Intermediate", "Advanced"], readonly=True, k="-skilllevel",
                                            enable_events=True),
                                   sg.Button("Reset Selection", k="-selectionreset")]],
                                   justification="center")]],
                                            title_location="n")]]


    window3 = sg.Window("Powder Ski Resort Guest Information", layout3, finalize=True, use_default_focus=False)
    window3.make_modal()

    showing3 = True

    while showing3:
        # updates total number of guests, if none it's displayed as the default value 0
        if tableinfo[0][1] == "-":
            pass
        else:
            window3["-guesttotal"].update(len(tableinfo))
        event3, values3 = window3.read()

        if event3 == sg.WINDOW_CLOSED:
            break

        if event3 == "-wantlessons":
            window3["-guesttable"].update(select_rows=tableRowSelection(tableinfo, "lessons", "none"))

        if event3 == "-wantequipment":
            window3["-guesttable"].update(select_rows=tableRowSelection(tableinfo, "equipment", "none"))

        if event3 == "-skilllevel":
            window3["-guesttable"].update(select_rows=tableRowSelection(tableinfo, "skilllevel", window3["-skilllevel"].get()))

        if event3 == "-selectionreset":
            window3["-skilllevel"].update("")
            window3["-guesttable"].update(select_rows=[])


layout0 = [[sg.Text("Welcome to Powder Ski Resort!", s=29, font=("Roboto", 20), justification="center",)],
           [sg.Image("skier1Corey.png")],
           [sg.Column([[sg.Button("I am a guest", enable_events=True, k="-guestbutton"),
                        sg.Button("I am a staff member", enable_events=True, k="-staffbutton")]],
                      justification="center")]]


window = sg.Window("Powder Ski Resort", layout0, finalize=True, use_default_focus=False)

# lists used later in table info and checking guest info
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
        createwindow3(guesttableinfo)
