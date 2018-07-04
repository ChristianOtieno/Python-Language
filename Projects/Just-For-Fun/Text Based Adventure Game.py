# name: Mr. Christian
# date: 2018-05-07
#description: Text-based space adventure game

import random
import time

def displayIntro():
    print("It is the end of a long year of fighting space criminals")
    print("you come to crossroads on your trip home, one path leads home")
    print("and the other leads through a game ray burst that will disintergrate you")
    print()

def choosePath():
    path = ""
    while path != "1" and path !="2": #inpt validation.
        path = input("Which path will you choose? (1 or 2): ")

    return path

def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("there's an asteroid nearby that looks familiar, that must be a good sign...")
    time.sleep(2)
    print("But your skin begins to tingle...")
    print()
    time.sleep(2)

    correctPath = random.randint(1,2)

    if chosenPath == str(correctPath):
        print("That tingling was just the feeling of admiration from the citizens of the galaxy!")
        print("Welcome home")
    else:
        print("An extremely energetic burst of gamma rays pass throogh you")
        print("causing all of the atoms in your body to dissociate")
        print("there is no record left of your existance")

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) #choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (yes or y to continue playing)")
