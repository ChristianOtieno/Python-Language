# Complete this function to return either
# "Hello, [name]!" or "Hello there!"
# based on the input

def say_hello(name):
    if name == input(name):
        print("Hello, {}".format(name))
    else:
        print("Hello there!")
        
name = input("What is your name? ")
say_hello(name) 
