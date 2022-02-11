# Corey Verkouteren
# 10/7/21 -
# Mr Ball's PM
# Using the message en/de-cryption GUI we made to de/en-crypt a file

# Password-based file Encrypter/Decrypter inside pySimpleGUI

# Note: all comments are made underneath of the code instead of above, changing with next new program probably

import PySimpleGUI as sg


def duprem(string):
    nwstring = ""

    for l in string:
        if l not in nwstring:
            nwstring += l

    return nwstring
# deletes duplicates from a string, if a duplicate is present, only the first instance is kept


def buildCypherString(password, decrypters):
    cpypassword = password

    for l in decrypters:
        chkr = cpypassword.count(l)

        if chkr == 0:
            cpypassword += l

    return cpypassword
# creates a "copy" of the/a original password and adds all characters present in a/the base string that are not present
# in the original password string to the end of the copied string, creating a unique cypher


def EnDeCryptdictMaker(cypherstr, basestr, ende):
    Cryptdic = {}

    if ende == "De":
        for i in range(len(basestr)):
            Cryptdic[basestr[i]] = cypherstr[i]

    elif ende == "En":
        for i in range(len(basestr) - 1):
            Cryptdic[cypherstr[i]] = basestr[i]

    return Cryptdic
# Creates a dictionary where the individual characters of the base string (basestr) and combination string (cypherstr)
# (created in the buildCypherString function) are the keys and values, the orders of these for decrypting and
# encrypting are important because it can cause decrypting errors if the orders are switched.


def endecoder(message, cyphdict):
    result = ""

    for l in message:
        chara = cyphdict.get(l, "nothing")

        if chara == "nothing":
            result += l

        else:
            result += chara

    return result


# uses the dictionary created with the EnDeCryptdictMaker function to decrypt or encrypt a message the user puts in.
# It does this by relating each character in the message to its key in the dictionary, grabbing the value of that key
# from the dictionary and adding it to the final encrypted or decrypted message (if it isn't there the character is just
# added)


def filewriter(contents, cyphdict, outfile):
    endecryptedmessage = ""
    with open(outfile, "w") as output:
        for line in contents:
            EnDecrypt = endecoder(line, cyphdict)
            output.write(EnDecrypt)
            endecryptedmessage += EnDecrypt


# writes to a/the file separate from the user's letter (that is meant to be encrypted or decrypted) with the encrypted or
# decrypted version of the user's letter, also updates the output on the window


# Main Program

sg.theme('DarkPurple4')

layout = [[sg.Frame("Password-Based File Decryptor/Encryptor", [
          [sg.Frame("Password", layout=[
              [sg.Input("", k="-pass")]],
                    vertical_alignment='center', element_justification="center", background_color="#53004c",
                    relief="flat", pad=10, title_location="n")],
          [sg.Frame("Input", layout=[
              [sg.FileBrowse("Browse Files", enable_events=True, k="-file", file_types=(("Text Files", ".txt"),)),
               sg.Input(readonly=True, disabled_readonly_background_color="#5a3d5c", tooltip="", k="-inf")],
              [sg.Text("Output", background_color="#53004c")],
              [sg.FileBrowse("Browse Files", enable_events=True, k="-ofile", file_types=(("Text Files", ".txt"),)),
                sg.Input(readonly=True, disabled_readonly_background_color="#5a3d5c", tooltip="", k="-ouf")]],
                    vertical_alignment='center', element_justification="center", background_color="#53004c",
                    relief="flat", title_location="n", pad=5)],
          [sg.Frame("Encrypt or Decrypt", layout=[
               [sg.Button(button_text="Encrypt", k="-ebutton", enable_events=True)],
               [sg.Button(button_text="Decrypt", k="-dbutton", enable_events=True)]],
                    vertical_alignment='center', element_justification="center", background_color="#53004c",
                    relief="flat", pad=5)],
          [sg.Text("File Status:"),
           sg.Text("Unchanged", k="-status")]],
                    relief="ridge", background_color='#2f0030', title_location="n", pad=5,
                    element_justification="center", title_color="#ff52f2")]]

window = sg.Window("", layout, resizable=True, finalize=True, use_default_focus=True, use_custom_titlebar=True,
                   titlebar_background_color="#200f21")

showing = True

Basestring = "zZ94aA1bBc0CeEg6GnNiIjJkK5mMoOqfFQd7DrR3sSlLtTpPuUv2VwW xX8yYhH"
# base used for encryption/decryption, includes a-z lower and upper, 1-9 + 0, and space

while showing:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-ebutton":
        Password = window["-pass"].get()

        finalpassword = duprem(Password)
        cypher = buildCypherString(finalpassword, Basestring)
        mode = "En"
        cypherdict = EnDeCryptdictMaker(cypher, Basestring, mode)

        efile = values["-file"]
        ofile = values["-ofile"]

        try:
            with open(efile, "r") as document:
                documentcont = document.read()
                filewriter(documentcont, cypherdict, ofile)
                window["-status"].update("Encrypted")

        except NameError:
            sg.popup_ok_cancel("File Does Not Exist")

        except FileNotFoundError:
            sg.popup_ok_cancel("One or Both Files Was Not Submitted")

    # If the "Encrypt" button is clicked, it gets the values from the "Password", "Output", and "Input fields and runs
    # the encryption on the contents of the file, writing the encrypted version into another file and showing it in
    # the output multiline

    elif event == "-dbutton":
        Password = window["-pass"].get()

        finalpassword = duprem(Password)
        cypher = buildCypherString(finalpassword, Basestring)
        mode = "De"
        cypherdict = EnDeCryptdictMaker(cypher, Basestring, mode)

        efile = values["-file"]
        ofile = values["-ofile"]

        try:
            with open(efile, "r") as document:
                documentcont = document.read()
                filewriter(documentcont, cypherdict, ofile)
                window["-status"].update("Decrypted")

        except NameError:
            sg.popup_ok_cancel("File does not exist")

        except FileNotFoundError:
            sg.popup_ok_cancel("One or Both Files Was Not Submitted")

    # If the "Decrypt" button is clicked, it gets the values from the "Password" and "file" fields and runs the
    # decryption on the contents of the file, writing the encrypted version into another file and showing it
    # in the output multiline
