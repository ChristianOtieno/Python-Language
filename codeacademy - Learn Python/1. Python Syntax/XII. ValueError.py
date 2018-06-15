#Python automatically assigns a variable the appropriate datatype
#based on the value it is given. A variable with the value 7
#is an integer, 7. is a float, "7" is a string.
#Sometimes we will want to convert variables to different datatypes.
#For example, if we wanted to print out an integer as part of a string,
#we would want to convert that integer to a string first.
#We can do that using str():

float_1 = 0.25
float_2 = 40.0

product = float(float_1) * float(float_2)

big_string = "The product was " + str(product) 

print(big_string)
