# Corey Verkouteren
# 9/7/21
# Mr Ball's Class
# Crazy Socks program

# Crazy Socks

import random as rdm

Colors = ["maroon", "cobalt", "sky blue", "teal", "purple", "black", "white", "crimson", "indigo", "brown",
          "saffron", "forest green", "lime", "violet", "hot pink", "tan", "orange", "gray", "silver", "magenta"]
Themes = ["model rocket", "car", "train", "dog", "pen", "star", "guitar", "surfboard", "polka-dot", "soda can", "cat",
          "vegetable", "dinosaur", "alphabet", "hat", "pickle", "book", "soccer ball", "tractor", "tree"]

TargetColor = rdm.choice(Colors)
TargetTheme = rdm.choice(Themes)
# Picks the target item from each list

rdm.shuffle(Colors)
rdm.shuffle(Themes)
# Shuffles each list

# Destructive read function


def TargetFinder(trgt, ctlist):
    # sets arguments, trgt is the one of the variables picked above, ctlist is one of the lists above
    working = True
    SearchCount = 0
    # sets a True variable and the beginning of the attempt counter
    while working:
        SearchCount += 1
        RandomChoice = ctlist.pop()
        # Counts each attempt and picks the last item of the shuffled list, setting it to RandomChoice
        if RandomChoice == trgt:
            working = False
        else:
            continue
        # Checks if the random choice from the list is the target, if it isn't the loop repeats, if it is then the
        # loop is ended (continue is only there because if it's not a pep8 error is there)
    RemainingInList = len(ctlist)
    return SearchCount, RemainingInList
    # Counts the remaining items in the list and returns the amount of attempts and remaining items in the list


# Main Program

print("Looking for", TargetColor, TargetTheme, "socks...")
# Shows the user what the target is from each list

TargetColorFound = TargetFinder(TargetColor, Colors)
TargetThemeFound = TargetFinder(TargetTheme, Themes)
# Uses the TargetFinder (destructive read) function to find the target in each list

NumberOfAttempts = TargetColorFound[0] + TargetThemeFound[0]
# Combines the number of attempts taken to find each target in the TargetFinder (destructive read) function

print("The", TargetColor, TargetTheme, "socks were found after", NumberOfAttempts, "total attempts, leaving only",
      TargetColorFound[1], "options left in the color list, and,", TargetThemeFound[1], "in the theme list")
# Shows the user the outputs (attempts, socks, and options left)
