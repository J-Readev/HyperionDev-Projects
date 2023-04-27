import math
import statistics

float_list = []

print("")

#Using a for loop in order to ask for 10 floats.
for x in range(10):
    #using .append to add to the list, getting input and converting to a float.
    float_list.append(float(input("Please enter a float:")))

print("")
#This will print out the total of all the numbers, using the sum function.
print(sum(float_list))

#Min & Max index of the list. Min to find the smallest number, and then .index to find where this is located. Same but with max for the next one.
print("")
print(float_list.index(min(float_list)))

print("")
print(float_list.index(max(float_list)))

#Average of the numbers and round off to 2 decimal places. Using statistics import as easiest method:
print("")
mean_floats=(statistics.mean(float_list))
print(round(mean_floats,2))

#Median number, same method as above.
print("")
print(statistics.median(float_list))
