"""
This program generates passages that are generated in mad-lib format
Author: Katherin 
"""

# The template for the story

STORY = ("This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world.")

print("Mad Libs has started")

name = input("Enter a name: ")
adjective1 = input("Enter your first Adjective: ")
adjective2 = input("Enter your second Adjective: ")
adjective3 = input("Enter your third Adjective: ")

verb = input("Enter a verb: ")

noun1 = input("Enter your first noun: ")
noun2 = input("Enter your second noun: ")

animal = input("Enter name for animal: ")
food = input("Enter name for a food: ")
fruit = input("Enter name a fruit: ")
superhero = input("Enter name for a superhero: ")
country = input("Enter for a country: ")
dessert = input("Enter name for dessert: ")
year = input("Enter an year: ")


print (STORY % (name, adjective1, adjective2, animal, food, verb, noun1, fruit, adjective3, name, superhero, name, country, name, dessert, name, year, noun2))



















