#function list_function has one argument called x.
#Inside the function, we return the item stored at index 1 of x.
#After the function, we create a new list called n.
#Finally, we call the list_function function with n as its argument,
#which prints out 55.

def list_function(x):
  return x[1]

n = [3, 5, 7]
print (list_function(n))
