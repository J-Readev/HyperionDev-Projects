
print("")

#This is opening the file so that it can be read.
file= open("dob.txt", "r")
#This is reading the lines of the file, allowing us to access the info.
lines=file.readlines()


#Printing out the names from the file.
print("     Name")
print("")

#In this section I am having to strip and split the file which is list.
for line in lines:
    temp = line.strip()
    temp = temp.split ()
    
    #I am now selecting which part of the file I want to use, which is the first two words of the name.
    names=str(temp[0:2])
    #I am now removing the brackets, commas etc from the names using .replace. 
    names=names.replace("[","")
    names=names.replace("]","")
    names=names.replace("'","")
    names=names.replace(",","")
    print(names)
    
print("")

#Now moving onto the birthdates it is the same process.
print("   Birthdate")
print("")

for line in lines:
    temp = line.strip()
    temp = temp.split ()
    

    #I am now selecting which part of the file I want to use, which is the first two words of the name.
    ages=str(temp[2:5])
    #I am now removing the brackets, commas etc from the names using .replace. 
    ages=ages.replace("[","")
    ages=ages.replace("]","")
    ages=ages.replace("'","")
    ages=ages.replace(",","")
    print(ages)

#Closing file so it doesnt keep using memory.
file.close()
print("")
