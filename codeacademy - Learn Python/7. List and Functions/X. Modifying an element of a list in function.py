#Changes list_function by:
#Adding 3 to the item at index 1 of the list.
#Then stores the result back into index 1.
#And returns the list.

def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print (list_function(n))
