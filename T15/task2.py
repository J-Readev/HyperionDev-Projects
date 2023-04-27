#Getting user inputs.
print("")
start_year=int(input("What year do you want to start with?: "))
print("")
year_amount=int(input("How many years do you want to check?: "))
print("")

#Displaying to user for clarity.
print("You have selected the year:",start_year)
print("")
print("You would like to check:",year_amount,"years")
print("")

#Any year that is divisible by 4 evenly, is a leap year.
#Setting the range, the limit will be how many years the user enters.
for x in range(0, year_amount):
    
    #This is to test if year is a leap year.
    if start_year %4==0:
        print(start_year,"is a leap year!")
        print("")
        #Need to increase the year by one each time to continue checking.
        start_year+=1

    else:
        print(start_year,"is not a leap year.")
        print("")
        start_year+=1
    