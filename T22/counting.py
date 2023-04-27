
#Creating string.
string ="google.com"

#Using a blank dictionary to loop through.
dictionary = {}

#For loop to loop through the string and count up how many letters there are that occur once or more.
for key in string:
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1

#Printing out the letters and their frequency.
print(dictionary)
