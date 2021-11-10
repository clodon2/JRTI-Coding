# Corey Verkouteren
# 11/9/21 - 11/10/21
# Mr. Ball's PM
# Object Oriented Programming (OOP)

# Draw Duplicates

import random as rd


class players:
    def __init__(self):
        self.cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
        self.target = ""
        self.matches = 0
        self.drawcount = 0

    def draw(self):
        draw = rd.choice(self.cards)
        if self.drawcount == 0:
            self.target = draw
        self.drawcount += 1
        return draw

    def matchcheck(self, card):
        if card == self.target:
            self.matches += 1

    def wincheck(self):
        if self.matches == 2:
            win = True
        else:
            win = False
        return win

    def resetgame(self):
        self.target = ""
        self.matches = 0
        self.drawcount = 0



def game(player, classplayer):
    # draws card
    drawncard = classplayer.draw()

    # checks for matches after you draw your target players
    if classplayer.drawcount > 1:
        classplayer.matchcheck(drawncard)

    # uses correct a/an (Grammar)
    aan = "a"
    if drawncard == 'Ace' or drawncard == 8:
        aan = "an"

    print(f"You drew {aan} {drawncard}")
    print(f"Target card: {classplayer.target}")

    # Uses plurals in the text responses correctly (Grammar)
    if classplayer.matches > 1 or classplayer.matches == 0:
        match = "matches"
    else:
        match = "match"

    if classplayer.drawcount == 1:
        pull = "pull"
    else:
        pull = "pulls"

    print(f"You have {classplayer.matches} {match} from {classplayer.drawcount} {pull}")
    # makes it easier to tell who just drew
    print()

    # checks for a win and returns it to main code with boolean
    end = False

    if classplayer.wincheck():
        print(f"{player} wins, resetting game")
        print()
        print("...")
        print()
        player1.resetgame()
        player2.resetgame()
        player3.resetgame()
        end = True

    return end


# Main --------------------------------------------------------------

playing = True

player1 = players()
player2 = players()
player3 = players()
currentplayer = ""

turn = 0

while playing:
    if turn > 3:
        turn = 1

    if turn == 1:
        currentplayer = "player1"
        print(f"Enter anything to draw, player{turn}")
        response = input()
        if response.lower() == "exit":
            playing = False
        else:
            winner = game("player3", player3)
            if winner:
                turn = 0

    elif turn == 2:
        currentplayer = "player2"
        print(f"Enter anything to draw, player{turn}")
        response = input()
        if response.lower() == "exit":
            playing = False
        else:
            winner = game("player3", player3)
            if winner:
                turn = 0

    elif turn == 3:
        currentplayer = "player3"
        print(f"Enter anything to draw, player{turn}")
        response = input()
        if response.lower() == "exit":
            playing = False
        else:
            winner = game("player3", player3)
            if winner:
                turn = 0

    elif turn == 0:
        print("Welcome to Draw Duplicates!")
        print("The goal of this game is to draw a duplicate card 5 times. Your first draw will be the 'target' card, "
              "the one you will have to draw 5 times.")
        print("Each turn you draw one card, first to 5 matches (duplicates drawn) wins. Enter 'exit' to end the game.")
        print()

    turn += 1
