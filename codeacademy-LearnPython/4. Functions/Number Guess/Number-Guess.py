from random import randint
from time import sleep

def GetUserGuess():
  guess = int(input("Enter your guesses: "))
  return guess
def RollDice(NumberOfSides):
  FirstRoll = randint(1, NumberOfSides)
  SecondRoll = randint(1, NumberOfSides)
  MaxVal = NumberOfSides * 2
  print ("The maximum number of sides will be: %d " % MaxVal)
  guess = GetUserGuess()
  if guess > MaxVal:
    print ("%d is too large." % guess)
  else:
    print ("Rolling...")
    sleep(2)
    print ("The first dice is %d" % FirstRoll)
    sleep(1)
    print ("The first dice is %d" % SecondRoll)
    sleep(1)
    TotalRoll = FirstRoll + SecondRoll
    print ("The total is %d" % TotalRoll)
    print ("Result...")
    sleep(1)
    if guess > TotalRoll:
      print ("You win!")
    else:
      print ("You lose!")
      
  RollDice(6)
  