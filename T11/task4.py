#Writing a program that asks for an integer and determines if it fits certain criteria.
#Getting int.
print("")
user_int=int(input("Please enter your desired integer, and I will tell some information about it: "))
print("")
print("The integer you have entered is:",user_int)
print("")

#Seeing if int is divisible by 2 and 5. If anything was above 0 it would mean that it would not be able to divide with no decimal places.
if (user_int%2==0) and (user_int%5==0):
    print("Your integer is divisible by 2 AND 5!")
    print("")

#Seeing if it can be divided by 2 but not 5.
elif (user_int%2==0) and (user_int%5!=0):
    print("Your integer is divisible by 2 but NOT 5!")
    print("")

#Seeing if it can be divided by 5 and not 2.
elif (user_int%2!=0) and (user_int%5==0):
    print("Your integer is NOT divisible by 2 but IS divisible by 5!")
    print("")

#Everything else would not be divisible by 2 or 5 so I can use an else statement.
else:
    print("Your integer is NOT divisible by 2 OR 5!")
    print("")
