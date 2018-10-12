# Branches and Functions

from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, You WIN!!!")
        exit(0)
    else:
        dead("You greedy bastard!!!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    print("CHOICES are: take honey OR taunt bear")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at you then claws your face off....")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now. type: open door to continue")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you FLEE for your life or WAIT for something to happen?")
    print("Choices: flee or wait ")

    next = input("> ")

    if "flee" in next:
        start()
    elif "wait" in next:
        dead("Cthulhu approaches you and suddenly rips your head Off and started chewing your nose....Well that was tasty!!!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Well done! Best decision of your LIFE!!!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()


# OUTPUT
# E:\GIT_DEV_python\venv\Scripts\python.exe E:/GIT_DEV_python/python_train/Exer35theHardWay.py
# You are in a dark room.
# There is a door to your right and left.
# Which one do you take?
# > left
# There is a bear here.
# The bear has a bunch of honey.
# The fat bear is in front of another door.
# How are you going to move the bear?
# > taunt bear
# The bear has moved from the door. You can go through it now.
# > open door
# This room is full of gold. How much do you take?
# > 1000
# You greedy bastard!!! Good job!
#
# Process finished with exit code 0


# note:
# input("> ") is a string that accepts input, that should print as a prompt before getting the users input










