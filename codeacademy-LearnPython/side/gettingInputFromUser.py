positiveNumber = None
while type(positiveNumber) is not int:
   try:
      positiveNumber = input("Please enter an integer: ")
      positiveNumber = int(positiveNumber)
      print("You entered: %d" % positiveNumber)
   except ValueError:
      print("%s is not an integer.\n" % positiveNumber)