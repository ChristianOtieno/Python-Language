#prompts the user for a hobby 3 times and saves the result of each in a variable called hobby then appends it to a variable called hobbies
hobbies = []

for num in range(3):
  hobby =  raw_input("Tell me one of your favorite hobbies: ")
  hobbies.append(hobby)

print (hobbies)
