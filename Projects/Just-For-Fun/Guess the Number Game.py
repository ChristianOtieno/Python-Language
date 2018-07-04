#Guess the Number Game
import random

guesses = 6
number = random.randint(1,100)
win  = False

while guesses > 0:
    guess = int(input("Your guess: "))

    if guess > number:
        print("Your gues was too high, you have", guesses, "remaining")
    elif guess < number:
        print("Your guess was too high, you have", guesses, "remaining")
    else:
        print("Congrats, you guessed the correct number, and won the game!")
        win = True

    guesses = 1
if win == False:
    print("Sorry, you didn't guess the right number, The right number was", number)
