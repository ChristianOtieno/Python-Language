#for-loop iterates over start_list and appends each number
#squared (x ** 2) to list then sorts it.

start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
  sqt = number ** 2
  square_list.append(sqt)
  square_list.sort()
print (square_list)
