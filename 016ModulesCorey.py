# Corey Verkouteren
# 11/2/21 - 1/3/21
# Mr Ball's PM
# Modules

import random as random


def addupname(Name):
    AUNalphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                   'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                   'x': 24, 'y': 25, 'z': 26}
    AUNresult = 0

    try:
        Name = Name.lower()
        Name = Name.replace(" ", "")
        for l in Name:
            AUNresult += AUNalphabet[l]

    except TypeError:
        AUNresult = "invalid name"

    except KeyError:
        AUNresult = "invalid name"

    except:
        AUNresult = "unknown error"

    if Name == "":
        AUNresult = "invalid name"

    return AUNresult


def setAlpha(visLevel):
    if visLevel == "nt":
        SAresult = 1

    elif visLevel == "st":
        SAresult = random.uniform(0.5, 0.9)

    elif visLevel == "vt":
        SAresult = random.uniform(0.2, 0.4)

    else:
        SAresult = "visibility level invalid"

    return SAresult


def setColor(theme):
    SCSPchoices = ["snow", "black", "gray50", "tan"]
    SCSOTchoices = ["medium slate blue", "forest green", "burlywood3", "red2", "midnight blue"]
    SCWACchoices = ["violet red", "chartreuse3", "goldenrod", "tomato", "HotPink1", "sienna3", "light sea green"]

    if theme == "Subdued/Professional":
        SCresult = random.choice(SCSPchoices)

    elif theme == "Slightly Out there":
        SCresult = random.choice(SCSOTchoices)

    elif theme == "Wild and Crazy":
        SCresult = random.choice(SCWACchoices)

    else:
        SCresult = "invalid theme option"

    return SCresult
