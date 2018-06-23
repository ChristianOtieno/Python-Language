#Defines a function called print_list that has one argument called x.
#then prints out each element one by one.
#Then calls the function with the argument n.
n = [3, 5, 7]

def print_list(x):
  for i in range(0, len(x)):
    print (x[i])
    
print_list(n)
