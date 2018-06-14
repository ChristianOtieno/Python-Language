def square(n):
    """Returns the square of a number."""
    squared = n **2
    print ("%d squared is %d." %(n, squared))
    return squared

square(10)

def shout(phrase):
    if phrase == phrase.upper():
        return ("You are shouting!")
    else:
        return ("Can you speak up?")

shout("I'M INTERESTED IN SHOUTING")
