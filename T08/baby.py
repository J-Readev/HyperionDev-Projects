#This task aims to demonstrate how to use Boolean functions in order to determine if someone is old enough to enter a party.
#The user needs to be 18 or older to gain entry.
print("")
print("In order to get in here, you need to be over 18.")
print("")
#I assign the birth year to a variable.
#I then ask for this using the input function, casting it as an integer.
user_birth_year=int(input("What year were you born?: "))
#I then minus the birth year from the current year to get the users age.
user_age=(2022-user_birth_year)
print("")
#I print out the users age to them.
print("You are:",user_age,"years old.")
print("")
#I use the if function to check whether the user is old enough.
#I use <= for anything equal to or less than 17.
#If I get this input, it prints out that the user is too young.
if user_age<=17:
    print("Sorry mate, you're not old enough. Come back when you're 18.")
#If the user is 18 or above, they get the congracts message using the if function and >=.
if user_age>=18:
    print("Congrats, you are old enough, come on in.")
