stringTwo = []

stringOne = str(input("Enter a list of strings: "))

stringTwo.append(stringOne)

stringTwo = [i.title() for i in stringTwo]
print(stringTwo)
