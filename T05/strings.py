#In this scenario I need to remove the "$" from an assigned variable.
#The task asks me to declare a variable called "hero" to be valued as "$$$Superman$$$"
#I have done this below.
("")
hero="$$$Superman$$$"
#I will print "Hero" to show the user what it looks like before it has been "stripped" of the "$".
print(hero)
#I am spacing this out to help with readability.
print("")
#Here I am using the print command to print out "hero" however I am then using it in conjunction with the "strip".
#I specify what I want to strip from the value by putting it in the brackets, ie: ("$")
print(hero.strip("$"))