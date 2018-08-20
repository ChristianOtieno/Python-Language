#A calculator that can compute the area of the various shapes.

print ("Calculator is starting")

option = input("Enter C for Circle or T for Triangle:")

if option == 'C':

  radius = float(input("Enter the radius of circle: "))
  area = 3.14159 * radius * radius
  
  print ("Area =", area)

elif option == 'T':
  
  base = float(input("Enter the base of the triangle: "))
  height = float(input("Enter the height of the triangle: "))
  area = 0.5 * base * height
  
  print ("Area =", area)

else:
  print ("You've entered an invalid shape.")

print ("Program is exiting.")
  
  
  
