# From https://www.souravsengupta.com/cds2015/python/LPTHW.pdf
# page 121

# Homework
# Now write a similar game to Exer25theHardWay.py It can be any kind of game you want in the same flavour.
# Spend a week on it, making it as interesting as possible. For Study Drills, use lists, functions, modules
# as much as possible, and find as many new pieces of Python as you can to make the game work.
# However, before you start coding, you must WRITE UP a MAP for your game. Create the rooms, monsters, and traps
# that the player must go through on paper before you CODE.

# Once you have your MAP, try to code it up. If you find problems with the map, then ADJUST IT and make the code MATCH.

# One final word of advice: ALL PROGRAMMERS BECOME PARALYZED BY IRRATIONAL FEAR STARTING A NEW LARGE PROJECT.
# They procrastinate to AVOID CONFRONTING THIS FEAR and end up not getting their program working or even started.
# I DO THIS. EVERYONE DOES. The best way to AVOID THIS is to MAKE A LIST of things you should do and then DO THEM ONE AT A TIME!!!

# JUST START DOING IT, DO A SMALL VERSION, MAKE IT BIGGER, KEEP A LIST OF THINGS TO DO, AND DO THEM!!!


# Game story:
# Intro

from sys import exit

def start():
    print("Welcome to the DnD where your magical dreams can be explored")
    print("Pick a character?")
    print("Warrior, Cleric, Mage, Orc, Sorcerer, Thief")

    next = input(">>>> ")

    if next == "Warrior":
        Warrior_stadium()
    elif next == "Cleric":
        Cleric_church()
    elif next == "Mage":
        Merlins_temple()
    elif next == "Orc":
        SwampLands()
    elif next == "Sorcerer":
        Hogwarts()
    elif next == "Thief":
        RobinHoodsLand()
    else:
        dead("You stumble around the room until you starve.")

def Warrior_training():
    print("You say to the squire: I am not ready, I shall sharpen thy skills and lift weights")
    print("So leave me alone and feed my horse")
    exit(0)

def dead(why):
    print(why, "Well done! Best decision of your LIFE!!!")
    exit(0)


def Warrior_stadium():
    print("You there!")
    print("You're the next Warrior class")
    print("Do you approach the stable or continue training?")
    print("Choices: approach or training ")

    next = input(">>>> ")

    if "approach" in next:
        Warrior_quest()
    elif "training" in next:
        Warrior_training()

    else:
        start()

def Cleric_church():
    print("Choices: approach or training ")

    # next = input(">>>> ")
    #
    # if "approach" in next:
    #     Warrior_quest()
    # elif "training" in next:
    #     Warrior_training("You say to the squire: I am not ready, I shall sharpen my skills and lift weights")
    #
    # else:
    #     start()


def Merlins_temple():
    print("Choices: approach or training ")

    # next = input(">>>> ")
    #
    # if "approach" in next:
    #     Warrior_quest()
    # elif "training" in next:
    #     Warrior_training("You say to the squire: I am not ready, I shall sharpen my skills and lift weights")
    #
    # else:
    #     start()


def SwampLands():
    print("Choices: approach or training ")

    # next = input(">>>> ")
    #
    # if "approach" in next:
    #     Warrior_quest()
    # elif "training" in next:
    #     Warrior_training("You say to the squire: I am not ready, I shall sharpen my skills and lift weights")
    #
    # else:
    #     start()

def Hogwarts():
    print("Choices: approach or training ")

    # next = input(">>>> ")
    #
    # if "approach" in next:
    #     Warrior_quest()
    # elif "training" in next:
    #     Warrior_training("You say to the squire: I am not ready, I shall sharpen my skills and lift weights")
    #
    # else:
    #     start()


def RobinHoodsLand():
    print("Choices: approach or training ")

    # next = input(">>>> ")
    #
    # if "approach" in next:
    #     Warrior_quest()
    # elif "training" in next:
    #     Warrior_training("You say to the squire: I am not ready, I shall sharpen my skills and lift weights")
    #
    # else:
    #     start()





def Warrior_quest():
    print("The Warrior saddles his horse and begins a journey ")
    print("Choices: dragon slaying, chopping ")

    next = input(">>>> ")

    if "approach" in next:
        Warrior_quest()
    elif "training" in next:
        Warrior_training("You say to the squire: I am not ready, I shall sharpen my skills and lift weights")

    else:
        start()

start()