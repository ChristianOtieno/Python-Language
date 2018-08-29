# Complete this function to return either
# "Hello, [name]!" or "Hello there!"
# based on the input

def say_hello(name):
  if name:
    name = input("What is your name? ")
    if name == input(name):
        print("Hello," + name + "!")
    else:
        return("Hello there!")
