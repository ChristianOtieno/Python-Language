while True:
    number = int(input("Positive Number: "))
    if number > 0:
        break
#print out this many rows        
for i in range(number):
    #print out this many columns
    for j in range(number):
        print("#",end="")
    print()
