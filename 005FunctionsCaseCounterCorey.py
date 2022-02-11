# Corey Verkouteren
# 9/2/2021-9/3/2021
# Mr Ball's class
# Learning about functions

# Case Counter
PCount = 0
UCount = 0
LCount = 0
running1 = True
# ^ sets all counting values to 0 and sets a true variable for the first while loop


def ULcount(strin, ucount, lcount):
    for L in strin:
        if L.count(L.upper()):
            ucount += 1
        elif L.count(L.lower()):
            lcount += 1
    return [ucount, lcount]


# ^ function for counting upper and lowercase letters
print("Welcome to Case Counter!")
while running1:
    PCount += 1
    running2 = True
    running3 = True
    while running2:
        theyInput = input("Please enter something containing only letters: ")
        if theyInput.isalpha():
            running2 = False
        else:
            print("You entered something other than letters, please try again")
            continue
# ^ checks that the input given contains only letters, since anything else causes errors
    Fcount = ULcount(theyInput, UCount, LCount)
    ULetters = Fcount[0]
    LLetters = Fcount[1]
# ^ uses the case counter function and separates it into the number of uppercase and lowercase letters
    print("You had", ULetters, "uppercase letters and", LLetters, "lowercase letters!")
# ^ prints the number of uppercase and lowercase letters
    while running3:
        theyInput2 = input("Would you like to play again? (yes or no): ")
        if theyInput2.lower() == "yes":
            print(" ")
            running3 = False
        elif theyInput2.lower() == "no":
            print("You have played", PCount, "time(s), thank you for playing!")
            running1 = False
            break
        else:
            print("That is not yes or no, please try again")
            continue
# ^ asks if they want to play again, displays number of times they played and quits if they say no. Asks again if they
# input something invalid.
