# Corey Verkouteren
# 11/9/21 - 11/15/21
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
        # picks a random card from self.cards and returns it, if it's the first draw that card is set as the target card
        draw = rd.choice(self.cards)
        if self.drawcount == 0:
            self.target = draw
        self.drawcount += 1
        return draw

    def matchcheck(self, card):
        if card == self.target:
            self.matches += 1

    def wincheck(self):
        # returns a true boolean if the player gets to 5 matches
        if self.matches == 5:
            win = True
        else:
            win = False
        return win

    def resetgame(self):
        # sets all variables to their original values, target is changed by draw attribute since drawcount is set to 0
        self.matches = 0
        self.drawcount = 0



def game(player, classplayer):
    # introduction instructions plus drawing the players
    print(f"{player}'s turn")
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
amount = 1

turn = 0

# instructions/about, gets rerun if inside loop
print("Welcome to Draw Duplicates!")
print("This game is meant for 3 players. "
        "The goal of this game is to draw a duplicate card 5 times. Your first draw will be the 'target' "
        "card, the one you will have to draw 5 times.")
print("Each turn you draw one card, first to 5 matches (duplicates drawn) wins. One turn is equal to one "
        "player's turn, so an input of 1 only plays the next player's turn, no on else's.")
print()

while playing:
    asking = True

    # runs for user set amount of turns
    for i in range(amount):
        # runs each player's turn by counting up and resetting the count to 1 if it's above 3 (or num of players)
        if turn > 3:
            turn = 1

        # player 1's turn
        if turn == 1:
            winner = game("player1", player1)
            # checks if the win value was returned as true
            if winner:
                turn = 0
                break

        # player 2's turn
        elif turn == 2:
            winner = game("player2", player2)
            if winner:
                turn = 0
                break

        # player 3's turn
        elif turn == 3:
            winner = game("player3", player3)
            if winner:
                turn = 0
                break

        turn += 1

    # gets the amount of turns user wants to play and sets it as amount (after casting to an integer), also allows
    # exiting of the game
    while asking:
        print("How many turns would you like to play? (input e to exit)")
        useramount = input()

        # ends game if user inputs e or E
        if useramount.lower() == "e":
            playing = False
            asking = False

        else:
            # casts useramount (input) and sets to amount, also catches errors from casting
            try:
                amount = int(useramount)
                asking = False

            except:
                print("Invalid number")
