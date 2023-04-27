print("")

#Getting input.
user_string=input("Hello, please give me a string: ")
print("")
#Showing user what they input.
print("Your string is:",user_string)
print("")

#Getting user character
user_char=input("What characters would you like to remove?: ")
print("")

#Making the new string using .replace in order to replace the users selected character with nothing.
#This results in the character being removed.
removed_char_string=user_string.replace(user_char,"")

print(removed_char_string)

