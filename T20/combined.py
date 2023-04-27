import random
#Importing random so I can generate random numbers for this task (needing to write them to a file).

#Creating File

ofile = open("numbers1.txt", "w")

#This sets up the list we will use.
random_numbers1_list=[]
print("")
#Asking the user how many inputs they would like.
num_amount=int(input("How many random numbers numbers would you like to write to 'numbers1.txt'?: "))
print("")

#This is a loop that will add however many random numbers to a list for the user. I used the imported random in order to achieve this.
for x in range (num_amount):
    #random number between 0-1000 each time.
    random_number=random.randint(0,1000)
    #This is then added to the list made earlier for however many times the user asks.
    random_numbers1_list.append(random_number)

#I will now need to sort the list before writing it to the text file. Storing as a variable.
num1_list_sorted=(sorted(random_numbers1_list))

#This will now write the sorted list to numbers1.txt.
ofile.writelines(str(num1_list_sorted))
#Closing file.
ofile.close()


#Now I am repeating the process to generate numbers2.txt. The process is the exact same but just a different number.

ofile = open("numbers2.txt", "w")

random_numbers2_list=[]

num_amount=int(input("How many random numbers numbers would you like to write to 'numbers2.txt'?: "))
print("")

for x in range (num_amount):
    random_number=random.randint(0,1000)
    random_numbers2_list.append(random_number)

num2_list_sorted=(sorted(random_numbers2_list))

ofile.writelines(str(num2_list_sorted))
#Closing file.
ofile.close()


#Now combining all numbers and writing them to the file.

ofile = open("all_numbers.txt", "w")
#Sorting and combining both lists.
all_numbers_sorted=sorted(random_numbers1_list+random_numbers2_list)
#writing it to the file.
ofile.writelines(str(all_numbers_sorted))
#Closing file.
ofile.close()


