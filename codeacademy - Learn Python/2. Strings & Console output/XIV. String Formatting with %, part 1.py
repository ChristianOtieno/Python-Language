#When you want to print a variable with a string,
#there is a better method than concatenating strings together.

#The % operator after the string is used to combine a string with variables.
#The % operator will replace the %s in the string with the string variable
#that comes after it.

string_1 = "Camelot"
string_2 = "place"

print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))
