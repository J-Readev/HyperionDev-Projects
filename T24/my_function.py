#Defining function to print all weekdays.
def Weekdays():

    print("")
    print("Sunday")

    print("")
    print("Monday")

    print("")
    print("Tuesday")

    print("")
    print("Wednesday")

    print("")
    print("Thursday")

    print("")
    print("Friday")

    print("")
    print("Saturday")


#Testing the function will print all weekdays as defined
Weekdays()

def add_hello(funct_string):

    changed_string = ""

    x = 0

    for word in funct_string.split():
        #Using this the below in order to detetmine where to add the hello.
        if x % 2 == 1:

            changed_string += "hello "

        else:  

            changed_string += word + " "

        x += 1
    #Removing spaces from end
    changed_string = changed_string[:-1]
    #Using return to give the final sentence.
    return changed_string

print("")
#Getting string from user, showing user string, and then using the function to replace the words.
input_string = input("Please enter a sting, then I will show you what I can do!: ")

print("")
print("Your string is:",input_string)
print("")
print("Now watch this!")
print("")
print(add_hello(input_string))
print("")

