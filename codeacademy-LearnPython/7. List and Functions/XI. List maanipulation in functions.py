n = [3, 5, 7]
#Defines a function called list_extender that has one parameter lst.
#Inside the function, we append the number 9 to lst.
#Then return the modified list

def list_extender(lst):
  lst.append(9)
  return lst
print list_extender(n)
