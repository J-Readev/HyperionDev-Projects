#Getting input.
print("")
user_input=input("Hello, please input a sentance: ")
print("")
#Using .split and a for loop I can split each whitespace from the word and print them in sucession.
for x in user_input.split():
    print(x)