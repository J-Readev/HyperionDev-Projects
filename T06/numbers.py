#For this task I need to ask the user to input three numbers and then complete maths with them.
print("")
#I begin by assigning the user's inputs to variables, num1,num2 and num3.
#I make sure to use the int() function to change the users number from a string to an integer.
#If I did not do this, I would not be able to use them in equations.
num1=int(input("Please enter your first number: "))
print("")
num2=int(input("Please enter your second number: "))
print("")
num3=int(input("Please enter your third number: "))
print("")
#Once I have gotten the numbers from the user, I display them back to them so they know what they have entered.
print("Your numbers are as follows:", num1, num2,num3)
print("")
#I assign the calculations to a variable so they can be used in the future.
#I need to caluclate the sum of all numbers.
#Using the "+" I can add the variables together with no issue as they are already integers.
#I print this for the user to see
sum_of_nums=(num1+num2+num3)
print("The sum of your numbers is:",sum_of_nums)
print("")
#I now need to take the first number and minus it by the second number.
#I do this by using "-" to minus one variable from another.
minus_num=(num1-num2)
print("Your first number minus your second number is:",minus_num)
print("")
#I now need to take the third number and then multiply it by the first.
#I do this by using the "*" sign, as this will multiply the variables by each other.
multiply_num=(num3*num1)
print("Your third number multiplied by your first is:",multiply_num)
print("")
#I now need to use the sum of all of the numbers and then divide it by the third number.
#I can do this because I already assigned the sum of all numbers to a variable.
#I use the "/" sign to divide the variable "sum_of_nums" (Sum of numbers made earlier) by the third number (num3)
sum_nums_divided=(sum_of_nums/num3)
#This is automatically set as a float because of the division.
#This could be changed, however it would mean that any decimals would be rounded, therefore not giving an accurate number.
#Therefore I am not changing this to an integer and leaving as a float.
print("the sum of your numbers, divided by your third number is:",sum_nums_divided)
print("")