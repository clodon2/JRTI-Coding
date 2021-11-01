# Corey Verkouteren
# 10/29/21
# Mr Ball's PM
# Make any window that has 2 tabs and can save information to a file, also has to make sense

# Message Appropriatizer

import PySimpleGUI as sg

sg.theme(new_theme="TealMono")

tab1 = [
    [sg.Multiline("Message Appropriatizer is a file editing tool meant to be used to edit emails or "
                  "other messages before you send them. Make sure you have your message written in "
                  "a .txt file that you can access on your computer. You can choose to edit your "
                  "message to be angry, incoherent, or informal. (yeah not really meant as a real "
                  "application)", disabled=True)]
]

tab2 = [
    [sg.FileBrowse("Choose File", enable_events=True, k="file", file_types=(("Text Files", ".txt"),)),
     sg.Input(readonly=True, enable_events=True, k="filedetect1")],
    [sg.Button("Angrify Message", enable_events=True, k="t2e")],
    [sg.Text("Message calm", k="t2s")]
]

tab3 = [
    [sg.FileBrowse("Choose File", enable_events=True, k="file2", file_types=(("Text Files", ".txt"),)),
     sg.Input(readonly=True, enable_events=True, k="filedetect2")],
    [sg.Button("Disfigure Message", enable_events=True, k="t3e")],
    [sg.Text("Message coherent", k="t3s")]

]

tab4 = [
    [sg.FileBrowse("Choose File", enable_events=True, k="file3", file_types=(("Text Files", ".txt"),)),
     sg.Input(readonly=True, enable_events=True, k="filedetect3")],
    [sg.Button("Relax Message", enable_events=True, k="t4e")],
    [sg.Text("Message not chilling", k="t4s")]
]

tab5 = [
    [sg.Button("Restore", enable_events=True, k="restore")],
    [sg.Multiline("Restores whichever document you edited last to its 'original' state. Only restores "
                  "from the last edit, so if you edited a document twice only the 2nd edit would be "
                  "reversed.", disabled=True)]
]


layout = [
    [sg.TabGroup([[sg.Tab("About", tab1),
                   sg.Tab("Angry", tab2),
                   sg.Tab("Incoherent", tab3),
                   sg.Tab("Informal", tab4),
                   sg.Tab("Restore", tab5)]])]
]

window = sg.Window("Message Appropriatizer", layout, finalize=True)

showing = True

while showing:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

# all of these if event "t_e"s basically do the same thing so I am going to address them all here,
    # opens the selected file, gets the contents of it, edits the contents (using string modifiers),
    # then writes the edited version to the file.
    if event == "t2e":
        file = values["filedetect1"]
        try:
            with open(file, "r") as document:
                documentcont = document.read()
                edocument = documentcont.upper()
            with open(file, "w") as document:
                document.write(edocument)
            window["t2s"].update("Message angrified")

        except NameError:
            sg.popup_ok_cancel("File Does Not Exist")

        except FileNotFoundError:
            sg.popup_ok_cancel("No File Submitted")

        window["filedetect1"].update("")

    elif event == "filedetect1":
        window["t2s"].update("Message calm")


    if event == "t3e":
        file = values["filedetect2"]
        try:
            with open(file, "r") as document:
                documentcont = document.read()
                # uses translation string modification, essentially whatever letter is in the right
                # string is turned into the corresponding one in the left string.
                translation = documentcont.maketrans('rRoOaAiI', 'wWuUeEyY')
                edocument = documentcont.translate(translation)
            with open(file, "w") as document:
                document.write(edocument)
            window["t3s"].update("Message incoherent")

        except NameError:
            sg.popup_ok_cancel("File Does Not Exist")

        except FileNotFoundError:
            sg.popup_ok_cancel("No File Submitted")

        window["filedetect2"].update("")

    elif event == "filedetect2":
        window["t3s"].update("Message coherent")


    if event == "t4e":
        file = values["filedetect3"]
        try:
            with open(file, "r") as document:
                documentcont = document.read()
                edocument = documentcont.lower()
            with open(file, "w") as document:
                document.write(edocument)
            window["t4s"].update("Message chilling")

        except NameError:
            sg.popup_ok_cancel("File Does Not Exist")

        except FileNotFoundError:
            sg.popup_ok_cancel("No File Submitted")

        window["filedetect3"].update("")

    elif event == "filedetect3":
        window["t4s"].update("Message not chilling")

# pulls the last used document and contents of it then replaces the current contents with the pulled ones.
    # This is only possible because multiple variables were used when reading and editing contents.
    if event == "restore":
        try:
            with open(file, "w") as document:
                document.write(documentcont)

        except NameError:
            sg.popup_ok_cancel("You have yet to edit any documents with this program.")
