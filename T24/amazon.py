#Opening the input file in order to read it. Then using encoding to prevent the error causing min to not be written.
input_file = open("input.txt", "r", encoding='utf-8-sig')
#Opening output file so it can be written to.
output_file = open("output.txt", "w")

#Getting the functions for Min.
def get_min(x):
    return min(x)

#Getting the functions for Max.
def get_max(x):
    return max(x)

#Getting the functions for Average.
def get_avg(x):
    return sum(x) / len(x)

#Using a for loop in order to get the numbers splitting them from the colon and stripping them of the commas.
for line in input_file:
    splitting = line.split(":")
    strip = splitting[0].strip().lower()
    nums = splitting[1].strip().split(",")
    #For loop again to convert to integers.
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    
    #Using if & elif to then write the required text to output file.
    #Using .join to bring everything together and writing it as the desired output. \n for new lines.
    if strip == "min":
        output_file.write("The min of [" + ", ".join([str(i) for i in nums]) + "] is " + str(get_min(nums)) + "\n")
    elif strip == "max":
        output_file.write("The max of [" + ", ".join([str(i) for i in nums]) + "] is " + str(get_max(nums)) + "\n")
    elif strip == "avg":
        output_file.write("The avg of [" + ", ".join([str(i) for i in nums]) + "] is " + str(get_avg(nums)))