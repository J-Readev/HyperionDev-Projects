print("")

string_1=input("Please give me a string: ")

print("")

#Need to work out how many chars are in the string so can use len. 
#Set as a variable so it can be used easier.
string_1_chars=(len(string_1))


#Will need to use a for loop for this in order to see whether it is an odd or even character.
#This can help determine if its needing to be upper() or lower()

#Defiining the alternate string so it can be combined.
alt_str= ""

#Using the variable we defined earlier for the amount of characters.
for x in range(string_1_chars):
    #Checking if it is even, if so it'll change that character to upper case.
    if x % 2 ==0:
        alt_str = alt_str + string_1[x].upper()
        #If not even, it'll be lower case.
    else:
        alt_str = alt_str + string_1[x].lower()

#Now the changed string will be printed for the user.
print("Here is your string with alternating cases: " + alt_str)

# Now I will need to make each alternative word upper/lower case.

#Converting the string into a split version of itself in order to use it.
split_str  = string_1.split()
#Here I will print the string out.
#I have to input " " in order to make sure the space is used in the full string.
# I then join it together after capitalising each other word.
#This is printing upper case.
print("")
print("Here is your string with alternate upper/lower case words:"," ".join(split_str[x].upper()
#I have to use an "&" here as "and" would not allow it to alternate. I had to look this up in order to use it on StackOverflow. 
if x & 1 
#Now this allows the code to print alternate words in lowercase.
#Having to use a for loop to alternate.
else split_str[x].lower() 
    for x in range(len(split_str))))

print("")