from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]

message = {"tie": "Yawn it's a tie!",
           "won": "Yay you won!",
           "lost": "Aww you lost!"}


def DecideWinner(UserChoice, ComputerChoice):
  print ("User Choice %s: " % UserChoice)
  print ("Computer Choice %s: " % ComputerChoice)
