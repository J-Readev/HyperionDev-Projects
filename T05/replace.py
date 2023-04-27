# In this task I must use the replace() function, the upper() function and then slicing in order to reverse the string.
# I start by assigning the variable a value which will need to be altered.
# I also space things out using ("") to help readability.
a_string="The!quick!brown!fox!jumps!over!the!lazy!dog!"
print("")
#With the variable assigned a value, I then print it so the user can see what it starts as.
print(a_string)
print("")
#I then need to use the replace() function in order to remove the "!" from the string and replace them with spaces.
#I do this below, by selecting the "!" by putting them in quotation marks, and then using a comma to space out what I need to replace it with.
#After the comma I put " " in order to detail what the function needs to change "!" to.
# #I also assign it to a varible in order to use it for other things.
#I then print this in order to show the change.
new_string=(a_string.replace("!"," "))
print(new_string)
print("")
#I now need to change this to upper case, so I will use the upper() function and assign it to a variable.
capital_string=(new_string.upper())
#This has now been changed, so I print it to show the use the change.
print(capital_string)
print("")
#I now need to print this in reverse. To do this I will need to slice it.
#To do this I set it as a new variable and use the previous variable that was made.
#I then add "[::-1}]" in order to reverse the string.
#I then print this in order to reverse it.
reverse_string=(capital_string[::-1])
print(reverse_string)
print("")
#However, when reversed, there is still the space at the end where the "!" was. I need to remove the first character of the string.
#To do this, I assign a it a new variable and the use "[1:]" to remove the first character.
#I then print the final outcome.
final_string=(reverse_string[1:])
print(final_string)
print("")