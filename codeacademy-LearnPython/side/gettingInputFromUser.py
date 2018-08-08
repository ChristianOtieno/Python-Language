positiveNumber = None
while type(positiveNumber) is not int:
   try:
      n = input("Please enter an integer: ")
      n = int(positiveNumber)
      print("You entered: %d" % positiveNumber)
   except ValueError:
      print("%s is not an integer.\n" % positiveNumber)