# Corey Verkouteren
# 9/10/21 -
# Mr Ball's class
# Dictionary practice

# give option to do 1k spins
# Who feels lucky?

import random as rdm


def FriendAdder(friend):
    Friends.append(friend)
    Scores[friend] = 0



Rewards = [1, 2, 3, 2, 5, 10, 1, 1, 2, 3, 5, 3]
Friends = []
Scores = {}

asking = True

print("Please input 5 of your friend's names:")
for i in range(5):
    FriendAdder(input())


while asking:
    answer = input("Would you like to spin the wheel, check the scores, or quit the game?(s,c, or q): ")
    if answer.lower() == "s":
        print("")
        Winner = rdm.choice(Friends)
        Reward = rdm.choice(Rewards)
        Scores[Winner] += Reward
        print(Winner, "got", Reward, "points!")
        print("")
    elif answer.lower() == "c":
        print("")
        print("The current scores are:")
        for Friends in Scores:
            print(Friends)
            print(Friends, "is at", Scores[Friends])
            print("")
        print(Friends)
    elif answer.lower() == "q":
        asking = False
    else:
        print("Something happened please try again")
print(Scores)
print(Friends)
