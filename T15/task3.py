
#Countdown from 20 to 0.
#Assining variable.
num=20

print("")
print("Here's a countdown from 20 to 0: ")
print("")

#Using while loop to minus one until num is less than or equal to 0.
while num >= 0:
    #Printing num (20 at this point).
    print(num)
    #Minusing one each time until condition is met,
    num -= 1
    print("")
    #Putting a break in so another loop can ocurr after.
    if num<0:
        break

#Loop displaying all even numbers between 1 and 20:

#Have to redefine the variable as above loops changed it.
num=20

print("Here is a loop that will display all even numbers between 1 and 20: ")

#Using a for loop as I find it's easier. Only need to find x in the range of 20, which is already num. Can start from 2 and go up 2 each time.
for x in range(2, num, 2):
    print("")
    print(x)

print("")

#Printing stars task:
print("Here are some stars, eventually becoming 5 stars: ")
print("")
# I found this easier to visualise by using variables. Nothing for this variable.
no_star=""

#Star that I'll use to add.
one_star="*"

#While loop to check if we have ***** if we dont add a star and print untill we do.
while no_star != "*****":
    no_star += one_star
    print(no_star)

    #Adding a break to make sure all stops.
    if no_star=="*****":
        break

print("")

#Finding the GCD.

print("")
print("I will help you find out the highest GCD from two positive integers.")
print("")

pos_int_1=int(input("Please give me your first positive integer: "))
print("")
pos_int_2=int(input("Please give me your second positive integer: "))
print("")

print("I will now find the highest common divisor between these two integers.")
print("")

#Using this code in order to determine what to divide by. the smaller number of the user's entered integers is to be used.
if pos_int_1<pos_int_2:
    number_used=pos_int_1
elif pos_int_2<pos_int_1:
    number_used=pos_int_2
else:
    number_used=pos_int_1

#Printing for user to see.
print("Since we want to find the the common denominator between", pos_int_1, "and", pos_int_2, "we can use the smaller number,",number_used,", as the demoninator can not be greater than the smallest number.")
print("")

#Using a while loop in order to figure out highest divisor.

while number_used>0:
    #This is to check if it is divisible with no recurring points.
    if (pos_int_1%number_used==0) and (pos_int_2%number_used==0):
        #Prints this and then breaks when highest GCD is found.
        print("The highest commmon divisor is", number_used)
        print("")
        break
    #Continues trying other options until highest denominator is found.
    else:
        number_used-=1
