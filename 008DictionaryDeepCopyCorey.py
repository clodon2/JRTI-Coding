# Corey Verkouteren
# 9/14/21 -
# Mr Ball's Class
# Dictionary of lists, deep copies

# Prize Picker

import random as rdm
import copy as cpy


def FriendAdder(friend):
    friend = friend.lower()
    friend = friend.title()
    if friend in Friends:
        print("Repeated name, please retry")
    else:
        Friends.append(friend)
        FriendsPrizes[friend] = cpy.deepcopy(FriendPrizeList)


# adds friends to the friend list and adds them to the FriendsPrizes dictionary as a key with their value being a deep
# copy of an empty list

# Main program

inputing = True
running = True

FriendsPrizes = {}
FriendPrizeList = []
Friends = []
PrizeList = ["Pencil", "Highlighter", "Notebook", "Pen", "Bookmark", "Marker", "Book"]

loopcounter = 0

print("Please enter 3 names:")
while inputing:
    CurrentFriends = len(Friends)
    if CurrentFriends < 3:
        FriendAdder(input())
    else:
        inputing = False
# has the user input 3 friends

while running:
    Loopx = input("How many times would you like to play?: ")
    if Loopx.isdigit():
        for i in range(int(Loopx)):
            ChosenFriend = rdm.choice(Friends)
            ChosenPrize = rdm.choice(PrizeList)
            FriendsPrizes[ChosenFriend].append(ChosenPrize)
        running = False
        # adds a random prize to a random friend's list in the FriendsPrizes dictionary x number of times
    else:
        print("That was not a number (NO LETTERS!)")
    # prevents errors involving casting

for key in FriendsPrizes:
    print(key, "has won a", FriendsPrizes[key])

# Prints the prizes each friend has
