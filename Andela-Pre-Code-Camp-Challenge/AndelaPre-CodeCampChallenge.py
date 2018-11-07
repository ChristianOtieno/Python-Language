stringTwo = []

#count = int(input("Enter list length: "))
stringOne = str(input("Enter a list of strings: "))
#for i in range (count):
stringTwo.append(stringOne)

#stringTwo.append( i.capitalize()) for [i] in stringOne] 
stringTwo = [i.title() for i in stringTwo]
print(stringTwo)
