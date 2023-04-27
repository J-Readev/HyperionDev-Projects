print("")
#Getting user input for age and storing as a variable.
age=int(input("Please enter your age: "))
print("")

#If statement for 18 or older, >= means greater than or equal to.
if age>=18:
    print("You are old enough!")
    print("")

#Elif for another if statement, using and to combine two checks.
elif age>16 and age<18:
    print("Almost there!")
    print("")

#Else for anything 16 and under as everything else has been given an outcome.
else:
    print("You're just too young!")
