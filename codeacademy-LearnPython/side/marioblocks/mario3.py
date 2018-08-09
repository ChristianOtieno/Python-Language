# prints a positive number of question marks, as specified by user

#prompts a user for a positive number
while True:
    number = int(input("Positive number: "))
    if number > 0:
        break
#Print out that many bricks
for i in range(number):
    print ("#")

