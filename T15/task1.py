print("")
user_num=int(input("Please enter a number, and I will print your times tables up to 12: "))


print("")
#Printing for user.
print("Your number is:",user_num)
print("")

#Using for loops, and 1 to 13 to make sure this goes up to the 12th times table.
for x in range (1, 13):
    #adding "x" and "=" so this comes out as a full equation. This will repeat until the 12th time. 
    print(user_num,"x",x,"=",(user_num*x))
    print("")