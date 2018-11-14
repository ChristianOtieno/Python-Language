#Define a variable x equal to 1
x = 1
#Start while loop until x != 1
while x == 1:
    #Prompt the user to enter a number
    number = input("Enter number: ")
    #Catch an exception, if a number is string keep x as 1
    #If not a string break from loop
    try:
        number1 = int(number)
        if number1 < 100 and number1 > 0:
            if number1 >= 0 and number1 <= 40:
                print("E")
            elif number1 > 40 and number1 <= 50:
                print("D")
            elif number1 > 50 and number1 <= 60:
                print("C")
            elif number1 > 60 and number1 <= 70:
                print("B")
            else:
                print("A")
            break
    except:
        print("Please enter a valid number")
