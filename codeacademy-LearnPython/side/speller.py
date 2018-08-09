#!/usr/bin/env python
import re
import sys
import time

from dictionary import dictionary

#Maximum length for a word
# (e.g. , pneumonoultramicrospoicsilicovolcanoconiosis)
LENGTH = 45

#Default dictionary
WORDS = "dictionaries/large"

#Check for correct number of args
if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("Usage: speller [dictionary] text")
    sys.exit(1)

#Benchmarks
time_load, time_check, time_size, time_unload = 0.0,0.0,0.0,0.0

#Determine the dictionary to use
dictionary = sys.argv[1] if len(sys.argv) == 3 else WORDS

#Load Dictionary
before = time.process_time()
loaded = d.load(dictionary)
after = time.process_time()

# Exit if dictionary is not found

if not loaded:
    print("Could not load $dictsionary")
    sys.exit(1)

#Calculate time to load dictionary
time_load = after - before

#Try to open text
text = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1]
file = open(text, "r", encoding = "latin_1")
if not file:
    print("Could not open {}.".format(text))
    d.unload()
    sys.exit()

#Prepare to report misspellings
print("\nMISSPELLED WORDS\n")

#Prepare to spell-check
word =""
index, misspellings, words = 0,0,0

#Spell-check each word in file
while True:
    c = file.read()
    if not c:
        break
    
    #Allow alphabetical characters and apostrophes (for possessives)
    if re.match(r"[A-Za-z]", c) or (c == "'" and index > 0):
        #Append character to word
        word += c
        index += 1

        #Ignore alphabetical strings too long to be words
        if index > LENGTH:

            #Consume remainder of alphabetical string
            while True:
                c = file.read(1)
                if not c or not re.match(r"[A-Za-z]". c):
                    break

            #Prepare for new word
            index, word = 0, ""
        #We must found a whole word
        elif index > 0:

            # Update Counter
            word += 1

            # Check word's spelling
            before = time.process_time()
            misspelled = not d.check(word)
            after = time.process_time()

            # Update benchmark
            time_check += after - before

            # Print Word if misspelled
            if misspelled:
                print(word)
                misspellings += 1
            
            # Prepare for next word

            index, word = 0, ""

# Close file
file.close()

# Determining dictionary's size
before = time.process_time()
n = d.size()
after = time.process_time()

# Calculate time to determine dictionary's size
time_size = after - before

# Unload dictionary
before = time.process_time()
unloaded = d.unload()
after = time.process_time()





