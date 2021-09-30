# Corey Verkouteren
# 9/27/21 - 9/30/21
# Mr Ball's PM
# Encrypting and Decrypting

# Password-based Encrypter/Decrypter


def duprem(string):
    nwstring = ""

    for i in string:
        if i not in nwstring:
            nwstring += i

    return nwstring
# deletes duplicates from a string, if a duplicate is present, only the first instance is kept


def buildCypherString(password, decrypters):
    cpypassword = password

    for i in range(0, len(decrypters)):
        chrctr = decrypters[i]
        chkr = cpypassword.count(chrctr)

        if chkr == 0:
            cpypassword += chrctr

    return cpypassword
# creates a "copy" of the/a original password and adds all characters present in a/the base string that are not present
# in the original password string to the end of the copied string, creating a unique cypher


def EnDeCryptdictMaker(cypherstr, basestr, ende):
    Cryptdic = {}
    edlcount = len(basestr)

    if ende == "De":
        for i in range(edlcount - 1):
            Cryptdic[basestr[i]] = cypherstr[i]

    elif ende == "En":
        for i in range(edlcount - 1):
            Cryptdic[cypherstr[i]] = basestr[i]

    return Cryptdic
# Creates a dictionary where the individual characters of the base string (basestr) and combination string (cypherstr)
# (created in the buildCypherString function) are the keys and values, the orders of these for decrypting and
# encrypting are important because it can cause decrypting errors if the orders are switched.


def endecoder(message, cypher):
    result = ""

    for l in message:
        chara = cypher.get(l, "nothing")

        if chara == "nothing":
            result += l

        else:
            result += chara

    return result
# uses the dictionary created with the EnDeCryptdictMaker function to decrypt or encrypt a message the user puts in.
# It does this by relating each character in the message to its key in the dictionary, grabbing the value of that key
# from the dictionary and adding it to the final encrypted or decrypted message (if it isn't there the character is just
# added)


# Main Program

using = True

while using:
    print("Please enter your password, or choose a new password (CASE SENSITIVE)")
    Password = input()

    Basestring = "zZ94aA1bBc0CeEg6GnNiIjJkK5mMoOqfFQd7DrR3sSlLtTpPuUv2VwW xX8yYhH"
    finalpassword = duprem(Password)
    # deletes duplicates from the entered password
    cypher = buildCypherString(finalpassword, Basestring)
    # creates the cypher, reference comment on buildCypherString

    asking = True
    deciding = True

    print("Enter your message:")
    msg = input()
    # all info used later, some input by user like the message and their password, base string includes all upper and
    # lower cases of the alphabet along with numbers 1-9, 0, and space. This is done so that if the password is weak,
    # the encryption appears to be much more complicated

    while asking:
        print("Would you like to encrypt or decrypt?(e or d)")
        eord = input()

        if eord.upper() == "E":
            mode = "En"
            Encrypt = EnDeCryptdictMaker(cypher, Basestring, mode)
            print("Your encrypted message is:", endecoder(msg, Encrypt))
            print("")
            asking = False
        # encrypts the message using the functions above if the user input is "e" or "E"

        elif eord.upper() == "D":
            mode = "De"
            Decrypt = EnDeCryptdictMaker(cypher, Basestring, mode)
            print("Your decrypted message is:", endecoder(msg, Decrypt))
            print("")
            asking = False
        # decrypts the message using the functions above if the user input is "d" or "D"

        else:
            print("That was not e or d")
            continue
        # prevents errors if e or d is not entered

    while deciding:
        print("Would you like to encrypt or decrypt again?(y or n)")
        cont = input()

        if cont.upper() == "Y":
            print("")
            deciding = False

        elif cont.upper() == "N":
            using = False
            deciding = False

        else:
            print("Invalid response, please try again")

        # either quits the program or returns them to the start of the "using" while loop (assuming valid input),
        # eliminates having to rerun the program if you want to do something else with it
