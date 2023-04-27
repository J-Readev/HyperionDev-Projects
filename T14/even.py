print("")

num=1

#Asking for users input.
user_num=int(input("Please enter a number: "))

print("")
print("You have entered the following:", user_num)
print("")


#Using while loops to get the numbers to repeat again and again.
#So while the number is NOT the users number, add one to 0.
while num != user_num:
    num += 1
    #This means that if the numbers are even, they should be printed.
    if num%2==0:
        print(num)
        print("")

    

    



