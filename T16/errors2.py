# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

#Lion is missing parentheses so it is not allowing animal to be defined. Syntax.
animal = "Lion"
animal_type = "cub"
#This will need to be converted to a string as it it needs to be added to other strings for the sentance below. Runtime.
number_of_teeth = str(16)

#There is no need for "{}" here. Syntax.
#Looks like the variables are in the incorrect location so they need swapping. Syntax Error.
full_spec = "This is a "+animal+". It is a "+animal_type+ " and it has "+number_of_teeth+" teeth"

#Missing Parentheses (Syntax Error).
print (full_spec)

