#.index(item) function is used to find the index of "duck",then assigns that result to a variable called duck_index.
#Then .insert(index, item) the string "cobra" at that index.
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index('duck') # Use index() to find "duck"
print (duck_index)
# Your code here!
animals.insert(2, 'cobra')

print (animals) # Observe what prints after the insert operation
