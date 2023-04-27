print("")

#Getting user string.
user_string=input("Hello, please enter a name: ")
#Capitalising the string to make sure the user input is formatted correctly, i.e "john" and "John" trigger the same result.
capital_user_string=user_string.capitalize()

#Setting up list in order to add to it.
string_list= []

#While loop to keep asking for an input if the user enters anything other than "John"
while capital_user_string != "John":
    #.append to add to the list.
    string_list.append(capital_user_string)
    #Asking the user to add another string to the list.
    print("")
    #Ensuring the loop asks for another name.
    user_string=input("Please enter another name: ")
    capital_user_string=user_string.capitalize()

    #This checks if John has been entered and will print the whole list if it is.
    if capital_user_string == "John":
        print("")
        print("John is the right name!")
        print("")
        print("The incorrect names you have entered are:",string_list)