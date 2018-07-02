import random

#A small function to welcome the user
def welcomeScreen():
    name = input("Enter your name: ")
    print("Welcome, ", name, "to the hangman game")
    print("#######################################")
    print("Try and guess the word in 6 tries or less")
    hangman()
    print()#Print a blank row



#start of the main program
def hangman():
    word = random.choice(["Subaru", "Ferrarri", "Mercedes", "Jeep",])
    validLetters ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    turns = 10
    guessef = ''

    while len(word) > 0:
        msg = ""
        missed = 0
        for letter in word:
            if letter in guessed:
                msg = msg + letter
            else:
                msg = msg + " " + " "
                missed += 1

        if msg == word:
            print(msg)
            print("You are correct, the word was: ", word)
            break

        print("Guess the word: ", msg)
        guess = input()

        if guess in validLetters:
            guessed = guessed + guess
        else:
            print("Enter a vslid letter: ")

            guess = input()
        if guess not in word:
            turns = turns -1
            if turns == 9:
                print("  0")
            if turns == 8:
                print("  0")
                print("  |")
            if turns == 7:
                print("  0")
                print("  |")
                print("  \ ")
            if turns == 6:
                print("  0")
                print("  |")
                print(" / ")
            if turns == 5:
                print("  0")
                print("  |")
                print(" / \ ")
            if turns == 4:
                print("  0")
                print("  |")
                print("_/ \_")
            if turns == 3:
                print("  0")
                print("  |-")
                print("_/ \_")
            if turns == 2:
                print("  0")
                print(" -|-")
                print("_/ \_")
            if turns == 1:
                print("You have failed to guess the word:", word)
                break

welcomeScreen()
                      
