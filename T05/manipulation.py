#For this task I will need to manipulate a users input/
#I start by asking the user for an input, and then assigning it a value which can be used.
print("")
str_manip=input("Hello! Please type any sentence you wish :) ")
print("")
print("You have input:",str_manip)
print("")
#I then need to show the user how many characters their sentance has. To do this the len() function.
#I assign this a value as it may need to be used in the future.
length_str_manip=len(str_manip)
#I then print this to display to the user.
print("Your input has",length_str_manip,"characters.")
print("")
#I then need to find the last letter of the user's entered sentance, and then replace every occurance of that letter with an "@".
#I can do this by using "[-1]" to get the last character.
#I assign this to a variable so it can be used later.
last_char=(str_manip[-1])
print("The last character of your input is:",last_char)
print("")
#Now I have the last character, I need to replace it in the users input.
#I make a new variable, and then use the replace() function in order to remove last_char and replace it with "@").
replaced_manip=str_manip.replace(last_char,"@")
#I then print this to display it.
print("I will now add @ in place of the reoccurance of the last character. Your input is now:", replaced_manip)
print("")
#I now need to print the last 3 characters of the string backwards. To do this I will need to reverse the string and then slice all but the last 3 characters.
#Below is the string reversed.
reversed_manip=(str_manip[::-1])
print("If I reverse your input you get:",reversed_manip)
print("")
#I then need to get the last 3 characters, or in this case, the first three as I have already reversed the string. 
#The last 3 characters have now become the first three.
#I use "[0:3]" in order to get these characters.
#I then print it as I have assigned it to a variable.
three_char_reversed_manip=reversed_manip[0:3]
print("The last three characters of your input, reversed, are:",three_char_reversed_manip)
print("")
#I now need to create a 5 letter word that is made up of the first 3 characters and the last two characters of str_manip.
#To do this I first find the first three characters and assign it a variable.
first_3_char_manip=str_manip[0:3]
#I now need to find the last two characters.
#I can do this using [-2:] as this allows me to locate the last two characters without having to know how many characters are in a string.
last_2_char_manip=str_manip[-2:]
#I now need to combine these two variables into a word.
#I use "+" instead of "," as this would separate the variables, where as I need no space between them as I words do not have this.
print("If I was to make a word using the first three characters and the last two characters of your input, I could make:",first_3_char_manip+last_2_char_manip)
print("")