# Corey Verkouteren
# 9/7/21
# Mr Ball's Class
# Crazy Socks program

# Crazy Socks
import random as rdm

Colors = ["Maroon", "Cobalt", "Sky Blue", "Teal", "Purple", "Black", "Titanium White", "Crimson", "Indigo", "Brown",
          "Saffron", "Forest Green", "Lime", "Violet", "Hot Pink", "Tan", "Orange", "Gray", "Silver", "Magenta"]
Themes = ["Model Rocket", "Car", "Train", "Dog", "Pen", "Star", "Guitar", "Surfboard", "Chair", "Soda", "Cat",
          "Countertop", "Refrigerator", "Scissors", "Hat", "Pickle", "Wire", "Soccer Ball", "Tractor", "Tree"]

TargetColor = rdm.choice(Colors)
TargetTheme = rdm.choice(Themes)
# Picks the target item from each list

rdm.shuffle(Colors)
rdm.shuffle(Themes)
# Shuffles each list


def TargetFinder(trgt, list):
    working = True
    SearchCount = 0
# sets a True variable and the beginning of the attempt counter
    while working:
        SearchCount += 1
        RandomChoice = list.pop()
# Counts each attempt and picks the last item of the shuffled list, setting it to RandomChoice
        if RandomChoice == trgt:
            working = False
        else:
            continue
# Checks if the random choice from the list is the target (continue is only there because if it's not its a pep8 error
    RemainingInList = len(list)
    return SearchCount, RemainingInList
# Counts the remaining items in the list and returns the amount of attempts and remaining items in the list


print(TargetColor, TargetTheme, "is the target")
# Shows the user what the target is from each list

TargetColorFound = TargetFinder(TargetColor, Colors)
TargetThemeFound = TargetFinder(TargetTheme, Themes)
# Uses the TargetFinder function to find the target in each list

NumberOfAttempts = TargetColorFound[0] + TargetThemeFound[0]

print("The target", TargetColor, TargetTheme, "was found after", NumberOfAttempts, "total attempts", ", leaving only",
      TargetColorFound[1], "options left in the color list, and,", TargetThemeFound[1], "in the theme list")
