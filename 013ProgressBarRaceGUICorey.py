# Corey Verkouteren
# 10//21 -
# Mr Ball's PM
# progress bar practice

# Progress Bar Race vs Computer

import PySimpleGUI as sg
import random as rd


def progressbarchoices(total):
    rchoice = rd.choice(Choices)
    total += rchoice
    if total <= 0:
        total = 0
    return rchoice, total


def gamereset():
    plyrtotal = 0
    cputotal = 0
    window["results"].update("")
    window["plyrp"].update(current_count=0)
    window["cpup"].update(current_count=0)
    window["racelength"].update("40", disabled=False)

    return plyrtotal, cputotal


sg.theme(new_theme="Topanga")

layout = [[sg.Frame("Welcome to the races!", [
          [sg.Input("40", enable_events=True, s=4, disabled_readonly_background_color="#393a32", k="racelength"),
           sg.Text("meter race")],
          [sg.Text("You", justification="left")],
          [sg.ProgressBar(orientation="horizontal", max_value=40, s=(40, 20), k="plyrp")],
          [sg.Text("CPU", justification="left")],
          [sg.ProgressBar(orientation="horizontal", max_value=40, s=(40, 20), k="cpup")],
          [sg.Button("Roll Movements", enable_events=True, k="rpick")],
          [sg.Multiline("Results", disabled=True, k="results")]],
                    title_location="n", element_justification="center")]]

window = sg.Window("Horse Race Simulator", layout, finalize=True, use_default_focus=True)

showing = True

Choices = [2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 10, 10, -2, -2, -6]
ChoicesResponse = {2: "horse has walked 2 meters", 4: "horse has ran 4 meters", 6: "horse has ran 6 meters",
                   8: "horse has dashed 8 meters", 10: "horse has sprinted 10 meters",
                   -2: "horse stumbled and lost 2 meters", -6: "horse got distracted and ran back 6 meters"}

window['plyrp'].update(0)
window['cpup'].update(0)

plyrtotal = 0
cputotal = 0

while showing:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "rpick":
        try:
            racemax = int(window["racelength"].get())
            window["plyrp"].update(current_count=plyrtotal, max=racemax)
            window["cpup"].update(current_count=cputotal, max=racemax)
            window["racelength"].update(disabled=True)

            window["results"].update("")

            plyrbar = progressbarchoices(plyrtotal)
            cpubar = progressbarchoices(cputotal)
            plyrtotal = plyrbar[1]
            cputotal = cpubar[1]

            window["results"].print("Player's " + ChoicesResponse[plyrbar[0]])
            window["results"].print("CPU's " + ChoicesResponse[cpubar[0]])

            window["plyrp"].update(plyrbar[1])
            window["cpup"].update(cpubar[1])

        except:
            window["racelength"].update(40)
            sg.popup("Race length invalid")

    if plyrtotal >= racemax:
        sg.popup("You have won the Game! Resetting the board....")
        plyrtotal = gamereset()[0]
        cputotal = gamereset()[1]

    elif cputotal >= racemax:
        sg.popup("CPU has won the Game! Resetting the board....")
        plyrtotal = gamereset()[0]
        cputotal = gamereset()[1]

    elif cputotal and plyrtotal >= racemax:
        sg.popup("What a race! You and CPU tied! Resetting the board...")
        plyrtotal = gamereset()[0]
        cputotal = gamereset()[1]
