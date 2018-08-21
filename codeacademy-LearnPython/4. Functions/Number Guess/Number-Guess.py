from random import randint
from time import sleep

def GetUserGuess():
    guess = int(input("Enter your guesses: "))
    return guess

def RollDice(NumberOfSides):
    guess = int(input("Enter your guesses: "))
    return guess

def RollDice(NumberOfSides):
  first_roll = randint(1, NumberOfSides)
  second_roll = randint(1, NumberOfSides)
  MaxVal = NumberOfSides * 2
  print ("The maximum number of sides will be %d " % max_val)
  guess = GetUserGuess()
  if  guess > MaxVal:
      print ("%d is too large.")

