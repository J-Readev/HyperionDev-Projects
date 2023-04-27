#In this scenario I need to gather information from the user and then present it at the end in a single sentance. To do this I must use variables.
#I begin by setting the scene.
#I am using the "print("")" command in order to space out my questions as it will look better for the end user. 
print("Hello there, I have a few questions to ask you! ")
print("")
#I will now begin to gather the information from the user by using the input commmand to ask a question and then storing it.
name=input("Please would you tell me your name? ")
print("")
age=input("What is your age? ")
print("")
house_number=input("What is your house number? ")
print("")
street_name=input("What is the name of your street? ")
print("")
#I will thank the user for providing this information. I have used the "=" in order to assign the users input to a variable, such as name or age. 
#This will then allow me to output this in the final sentance.
print("Thank you for providing this information!")
print("")
#In this sentance I use the print command to show the user the sentance. I use quotation marks for the pieces of text that aren't variables.
#I separate the sentances and the variables with commas in order to ensure that the sentance will print correctly and not produce an error. 
print("I have been speaking with", name, "who is", age, "and lives at house number", house_number, "on", street_name)
