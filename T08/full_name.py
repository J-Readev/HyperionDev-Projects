print("")
#Assign input to a variable.

user_name=input("Please enter your full name: ")

print("")
#I use IF and LEN to count how many characters is in the input. 
#I then use ==0 to print the following if nothing has been entered.
if len(user_name)==0:

    print("You haven't entered anything. Please enter your full name.")

#I have to use LEN <4 and >=1 as otherwise both statements would display when entering no characters, as entering nothing is less than 4.
if len(user_name)<4 and len(user_name)>=1:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname")

#LEN again, asking for less than 25 character.
if len(user_name)>25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your name.")

#I then run a check for the correct name.
#I use AND to combine the two len statements into the one if statement.
#I learned this during my application process.
if len(user_name)<=25 and len(user_name)>=4:
    print("Thank you for entering your name", user_name)