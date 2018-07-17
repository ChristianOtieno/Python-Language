from random import randint
#This exercise, allow the user to guess what the number is 3 times

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start of the game
while guesses_left > 0:
  guess = int(raw_input("Your guess: "))
  if guess == random_number:
    print ("You win!")
    break
  guesses_left -= 1
else:
  print ("You lose.")
