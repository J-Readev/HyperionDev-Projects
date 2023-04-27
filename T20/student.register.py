
#Creating a file called output and allowing it to be written to.
ofile = open('reg_form.txt', 'w')


#Asking for the amount of students from the user.
print("")
student_number= int(input("How many students do you need to register? :"))
print("")

#Creating a loop for the amount that the user enters.
for x in range (student_number):
    #Asking for student ID.
    student_id = input("Enter a student ID: ")
    print("")
    #Writing this to the file.
    ofile.write(student_id+"            ....................."+"\n")

#Commenting on the file what the numbers mean.
ofile.write("\n"+"Listed above are the registered student ID that have been registered. Please sign on the line to confirm attendance")

#Closing file.
ofile.close()