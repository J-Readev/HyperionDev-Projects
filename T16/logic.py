print("")

#Showing a logical error to the user.
print("Hey there! Let me show you a logical error!")
print("")

#Getting user int.
first_num = int(input("Please can you enter an integer: "))
print("")

#Getting second int. 
second_num = int(input("Please enter another integer: "))
print("")

#Working out the average. This will result in a logical error as this runs, but due to the lack of brackets the division will happen first.
#This will not produce the average correctly.

calulation_result = first_num+second_num/2

print("Your average is: ",calulation_result)
print("")

print("This is a logical error because although the code runs, the answer is incorrect.")