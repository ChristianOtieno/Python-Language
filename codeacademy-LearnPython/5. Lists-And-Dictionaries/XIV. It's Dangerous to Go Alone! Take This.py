inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Adding a key 'pocket' to inventory and assigning a list to it
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
# Sorting 'backpack' in inventory
inventory['backpack'].sort()

inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50

print (inventory)
