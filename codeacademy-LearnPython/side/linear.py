import sys

#Names in a phone book
book = [
    "ALex",
    "Brian",
    "Charles",
    "Derrick",
    "Everline",
    "Frankline",
    "MacDaniel",
    "Nathaniel",
    "Suleiman",
    "Kennedy",
    "Michael"]
#Prompts user for name
name = str(input("Name: "))
if name in book:
    if name[0].isupper() or name[0].islower():
        print(f"Calling... {name}")
else:
    print(f"Quitting... {name}")
