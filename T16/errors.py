# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

#This is causing an error as it is not bracketed for the print statement.Syntax.
print ("Welcome to the error program")
#No brackets and has unexpected indent.Syntax.
print ("\n")

#Indent issue again. Syntax. 
#Needs to be defined using "=" not "==". Syntax. 
#No need to specify "years old". Runtime.
ageStr = 24  
#Indent Issue. Syntax.
age = int(ageStr)
#Indent Issue. Syntax.
#Need to use commas for correct spacing. Syntax.
print("I'm" , age , "years old.")
#Shouldnt have "". Syntax.
three = 3

#Indent Issue.Syntax.
answerYears = age + three

#No brackets.Syntax.
#Should not have "" around answerYears as it is a variable. Syntax.
#Should use comma not "+" as combining strings and ints. Runtime.
print ("The total number of years:" , answerYears)

#Cannot run as answer is not defined. Runtime. 
#Answer has to be 27.5 as 330 / 12 = 27.5.
answer=27.5
answerMonths = answer * 12
#Missing Brackets. Syntax.
#Commas not "+". Syntax.
print ("In 3 years and 6 months, I'll be " , answerMonths , " months old")

#HINT, 330 months is the correct answer

