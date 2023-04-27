#Assigning Variables.
num1=1
num2=2
num3=3

#Printing for user.
print("")
print("Variable 1 is:",num1)
print("")
print("Variable 2 is:",num2)
print("")
print("Variable 3 is:",num3)
print("")

#Comparing num1 & num2, if num 1 is bigger than num 2 it will print num 1, if it is the larger value.
if num1>num2:
    print("Between variable 1 and variable 2 the larger value is:",num1)
    print("")
#There are only two variables to compare so I can use else.
else:
    print("Between variable 1 and variable 2 the larger value is:",num2)
    print("")

#To determine if num1 is off or even.
#I will need to see if the number can be divided by 2 and = 0 for the remainder as all even numbers will do this.
if int(num1%2)==0:
    print("Variable 1 is even.")
    print("")
else:
    print("Variable 1 is odd.")
    print("")

#Sorting the three numbers from largest to smallest.
#Finding smallest:
if num1>num2 and num1>num3:
    print("The first number is:",num1)
    print("")
elif num2>num1 and num2>num3:
    print("The first number is:",num2)
    print("")
else:
    print("The first number is:",num3)
    print("")

#Finding middle number:
if num1<=num2 <=num3 or num3<=num2<=num1:
    print("The middle number is:",num2)
    print("")
elif num2 <= num1 <=num3 or num3 <=num1 <=num2:
    print("The middle number is:",num1)
    print("")
else:
    print("The middle number is:",num3)
    print("")

#Finding largest:
if num1<num2 and num1<num3:
    print("The last number is:",num1)
    print("")
elif num2<num1 and num2<num3:
    print("The last number is:",num2)
    print("")
else:
    print("The last number is:",num3)
    print("")
