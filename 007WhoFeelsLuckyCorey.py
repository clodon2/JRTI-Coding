# Corey Verkouteren
# 9/10/21 - 9/13/21
# Mr Ball's class
# Dictionary practice

# Who feels lucky?

import random as rdm


def FriendAdder(friend):
    friend = friend.lower()
    friend = friend.title()
    if friend in Friends:
        print("Repeated name, please retry")
    else:
        Friends.append(friend)
        Scores[friend] = 0
    # detects repeated names (inputs) and adds new names (inputs) to the dictionary and list


# Main Program

Rewards = [2, 2, 2, 2, 2, 4, 4, 4, 4, 6, 6, 6, 8, 8,  10]
Friends = []
Scores = {}

asking = True
inputing = True


print("Please input 5 of your friend's names (input the first name then press enter, etc.):")
while inputing:
    CurrentFriends = len(Friends)
    if CurrentFriends < 5:
        FriendAdder(input())
    else:
        inputing = False
# Has the user input their friends, and makes it impossible to put in duplicate names

while asking:
    answer = input("Would you like to spin the wheel, check the scores, or quit the game?(s,c, or q): ")

    if answer.lower() == "s":
        print("")
        Winner = rdm.choice(Friends)
        Reward = rdm.choice(Rewards)
        Scores[Winner] += Reward
        print(Winner, "got", Reward, "points!")
        print("")
    # Gives a random friend a random score based on the lists

    elif answer.lower() == "c":
        print("")
        print("The current scores are:")
        for key in Scores:
            print(key, "is at", Scores[key], "points")
            print("")
    # prints the current score individually for each friend

    elif answer.lower() == "q":
        print("")
        HighestScore = 0
        Champion = ""
        for key in Scores:
            KeyScore = Scores[key]
            if KeyScore > HighestScore:
                HighestScore = KeyScore
                Champion = key
            elif KeyScore == HighestScore:
                ChampionsList = [key, Champion]
                Champion = rdm.choice(ChampionsList)
            else:
                continue
        # finds the highest key value in the Scores dictionary, if there is a tie it picks a random winner from the tie
        print("Thank you for playing,", Champion, "has won the game")
        asking = False
    # quits the game and prints the winner

    else:
        print("")
        print("Something happened, please try again")
        print("")
    # ends the if/else statements, prevents errors
