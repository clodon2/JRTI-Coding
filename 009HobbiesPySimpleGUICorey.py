# Corey Verkouteren
# 9/21/21 - 9/23/21
# Mr Ball's class
# PySimpleGUI practice

# Guitar lister

import PySimpleGUI as sg

newtheme = {'BACKGROUND': 'black', 'TEXT': 'white', 'INPUT': '#313131', 'SCROLL': '#313131',
                 'TEXT_INPUT': 'white', 'BUTTON': ('white', '#313131'), 'PROGRESS': '#313131', 'BORDER': 0,
                               'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

sg.theme_add_new('blackgray', newtheme)

sg.theme('blackgray')

layout = [[sg.Text('Guitar Lister', justification='center', size=(60, 1))],
          [sg.Text("Please enter the make and model of the guitar:", justification='center')],
          [sg.InputText("", size=(20, 1), key='-inputb', enable_events=True)],
          [sg.Text("What kind of guitar is it?")],
          [sg.Radio("Electric", enable_events=True, group_id='g1', key='-r1'),
           sg.Radio("Acoustic", enable_events=True, group_id='g1', key='-r2'),
           sg.Radio("Classical", enable_events=True, group_id='g1', key='-r3')],
          [sg.Text("Please list the condition of the guitar:")],
          [sg.Checkbox("Has Strings", enable_events=True, key='-c1'),
           sg.Checkbox("Working/Functional", enable_events=True, key='-c2'),
           sg.Checkbox("Modified", enable_events=True, key='-c3'),
           sg.Checkbox("For Parts", enable_events=True, key='-c4')],
          [sg.Combo(values=['Mint', 'Near Mint', 'Minimal Wear', 'Mild Wear', 'Heavy Wear'], key='-con',
                    background_color='#313131', enable_events=True)],
          [sg.Text("How much work does the guitar need?", key='-wrk')],
          [sg.Slider(range=(0, 10), resolution=0.5, orientation='h', relief='flat', key='-wrksl')],
          [sg.Button(button_text='Reset all', key='-clr'), sg.Button(button_text='Submit/Save', key='-sbmt')],
          [sg.InputText("Not Submitted", readonly=True, background_color="black", key='-status',
                        disabled_readonly_background_color="black", enable_events=True)]]

window = sg.Window('Guitar Lister', layout, resizable=True, finalize=True, background_color='black',
                   use_default_focus=True, button_color='#313131')

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == '-clr':
        window['-inputb'].update("")
        window['-r1'].update(value=False)
        window['-r2'].update(value=False)
        window['-r3'].update(value=False)
        window['-c1'].update(value=False)
        window['-c2'].update(value=False)
        window['-c3'].update(value=False)
        window['-c4'].update(value=False)
        window['-con'].update("")
        window['-status'].update("Not Submitted")
        window['-wrksl'].update(value=0)

    elif event == '-sbmt':
        window['-status'].update("Submitted")

    elif event:
        window['-status'].update("Not Submitted")



    if values['-con'] == 'Mint':
        print("wrk")
        window['-wrk'].hide_row()
        window['-wrksl'].hide_row()

    else:
        window['-wrk'].unhide_row()
        window['-wrksl'].unhide_row()
        continue
