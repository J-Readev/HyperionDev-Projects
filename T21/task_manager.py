#=====importing libraries===========
from datetime import date

#====Login Section====

print("")

#Opening the user.txt file in order to check password / username is correct.
open_file = open("user.txt","r")
#Reading the file once open.
lines = open_file.readlines()

#Getting username to determine if they can log in.
user_username = input("Please enter your username: ")
print("")

#I am stripping and splitting the username and password from the file.
for line in lines:
    temp = line.strip()
    temp = temp.split ()


    #I am now selecting which part of the file I want to use, which is the first word (user name)
    filed_username=str(temp[0])
    #I am now removing the brackets, commas etc from the names using .replace. 
    filed_username=filed_username.replace("[","")

    filed_username=filed_username.replace("]","")

    filed_username=filed_username.replace("'","")

    filed_username=filed_username.replace(",","")

    if filed_username==user_username:
        print("You have entered a valid username.")
        print("")
        #Break needed to keep loop working after text file is edited.
        break
    else:
        while filed_username != user_username:
            user_username=input("You have not entered a correct username. Remember this will be case sensitive. Please try again: ")
            print("")

            if filed_username == user_username:
                print("You have entered a correct username")
                print("")
        break



#Getting user password to see if they can log in.
user_password = input("Please enter your password: ")
print("")

for line in lines:
    temp = line.strip()
    temp = temp.split ()

    #I am now selecting the password.
    filed_password=str(temp[1])
    #I am now removing the brackets, commas etc from the password using .replace. 
    filed_password=filed_password.replace("[","")

    filed_password=filed_password.replace("]","")

    filed_password=filed_password.replace("'","")
    
    filed_password=filed_password.replace(",","")

    if filed_password == user_password:
        print("Your password is correct.")
        print("")
        #Break needed to keep loop working after text file is edited.
        break
    else:
        while filed_password != user_password:
            user_password=input("You have not entered the correct password for this username. Remember this will be case sensitive. Please try again: ")
            print("")

            if filed_password==user_password:
                print("You have entered a correct password")
                print("")
        break
    
print("Welcome",user_username,"you have gained access to the system as you have entered your details correctly")
open_file.close

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
 print("")
 menu = input('''Select one of the following Options below:

r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit

: ''').lower()

 if menu == 'r':
    pass

    if user_username != "admin":
        print("You do not have admin rights, therefore you are unable to register users. Please contact your admin to do this")
    
    elif user_username == "admin":
        
        print("")
        print("Admin permissions granted. Please select one of the options below.")
        print("")
        admin_input = input("r - register user, d - display statistics :").lower()

        if admin_input == "r":

            print("")
            new_username = input("Please enter the username of the new user you would like to register. Remember this is case sensitive: ")
            print("")

            new_user_password = input("Please enter the password for the new user. Remember that this is case sensitive: ")
            print("")

            new_user_password_confirmation = input("Please enter the password again in order to confirm this password: ")

            #Using a while loop in order to ensure passwords all match. This will loop untill passwords match.
            while new_user_password != new_user_password_confirmation:
                    print("")
                    print("This password does not match the password you have entered above.")
                    print("")
                    new_user_password = input("Please enter the password for the new user. Remember that this is case sensitive: ")
                    print("")
                    new_user_password_confirmation = input("Please enter the password again in order to confirm this password: ")

            print("")
            print("You have added the user:",new_username)
            print("")
            print("Their password is:",new_user_password_confirmation)
            print("")
            print("Please ensure that the new user changes their password to something of their own choosing as soon as possible.")
            print("")

            #Writing to file.
            open_file = open("user.txt","a")
            open_file.writelines("\n")
            open_file.writelines(new_username+", ")
            open_file.writelines(new_user_password)
            
            #closing file as is no longer in use.
            open_file.close
        
        #This will open the statistics menu.
        elif admin_input == "d":
            
            #Setting variables at 0.
            num_of_tasks = 0
            num_of_users = 0

            open_file = open("tasks.txt","r")
            
            #counting the lines in the file, as this will correlate to the amount of taks.
            for line in open_file:
                num_of_tasks += 1

            print("")
            print("The total number of tasks is: ", num_of_tasks)
            open_file.close

            open_file = open("user.txt","r")
            #Counting lines.
            for line in open_file:
                num_of_users += 1

            print("")
            print("The total number of users is: ", num_of_users)
            open_file.close()
        
        #Sending back to the menu if incorrect option is entered.
        else:
            print("")
            print("You have not chosen a correct option. Please reload and try again.")

 elif menu == 'a':
        pass
        
        #Will use append as to not overwite the data in the file.
        open_file = open("tasks.txt","a")

        #Getting user inputs.
        tasked_username = input("You are assigning a user a task. Please confirm which user you would like to assign a task to: ")
        print("")
        tasked_title = input("Please input the title of the task you wish to assign: ")
        print("")
        tasked_description = input("Please enter a brief description of the task: ")
        print("")
        tasked_deadline = input("Please enter the due date of this task (DD/MM/YY): ")

        #As I imported date, I can get todays date easily like so. I learned how to do this through Programiz.
        today = date.today()
        todaysdate = today.strftime("%d/%m/%Y")

        #Writing everything to the file.
        open_file.writelines("\n")
        open_file.writelines(tasked_username+", ")
        open_file.writelines(tasked_title+", ")
        open_file.writelines(tasked_description+", ")
        open_file.writelines(todaysdate+", ")
        open_file.writelines(tasked_deadline+", ")
        open_file.writelines("No")
        
        #Closing file.
        open_file.close
        

 elif menu == 'va':
    pass
    #Opening the file again as it was closed.
    open_file = open('tasks.txt', 'r+')
    #Now reading the lines on the file.
    Lines = open_file.readlines()
    #Printing for spacing.
    print("")

    #For loop to read and print each line.
    for line in Lines:
    #Stripping and Splitting the sentances so that they can be printed separately.
        temp = line.strip
        temp = line.split(",")

        #Assiging all of the sentances to variables so they can be used.
        task_name = str(temp[1])
        task_owner = str(temp[0])
        task_date_assigned = str(temp[3])
        task_due_date = str(temp [4])
        task_state = str(temp[-1])
        task_desc = str(temp[2])

        #Removing all of the stuff that exists as it is a list.
        task_name=task_name.replace("[","")
        task_name=task_name.replace("]","")
        task_name=task_name.replace("'","")
        task_name=task_name.replace(",","")

        task_owner=task_owner.replace("[","")
        task_owner=task_owner.replace("]","")
        task_owner=task_owner.replace("'","")
        task_owner=task_owner.replace(",","")

        task_desc=task_desc.replace("[","")
        task_desc=task_desc.replace("]","")
        task_desc=task_desc.replace("'","")
        task_desc=task_desc.replace(",","")

        task_date_assigned=task_date_assigned.replace("[","")
        task_date_assigned=task_date_assigned.replace("]","")
        task_date_assigned=task_date_assigned.replace("'","")
        task_date_assigned=task_date_assigned.replace(",","")

        task_due_date=task_due_date.replace("[","")
        task_due_date=task_due_date.replace("]","")
        task_due_date=task_due_date.replace("'","")
        task_due_date=task_due_date.replace(",","")

        task_state=task_state.replace("[","")
        task_state=task_state.replace("]","")
        task_state=task_state.replace("'","")
        task_state=task_state.replace(",","")

        #Printing all of the tasks in Output 2 method as requested.
        print("___________________________________________________________")
        print("")
        print ("Task:            ",task_name)
        print ("Assigned to:      ",task_owner)
        print ("Date assigned:   ",task_date_assigned)
        print ("Due date:        ",task_due_date)
        print ("Task Complete?:  ",task_state)
        print("Task description:")
        print(task_desc)
        print("___________________________________________________________")

 elif menu == 'vm':
        pass

        #Opening the file again as it was closed.
        open_file = open('tasks.txt', 'r+')
        #Now reading the lines on the file.
        Lines = open_file.readlines()

        print("")

        #For loop to read and print each line.
        for line in Lines:
            #using an if statement to ONLY print the user's username tasks.
            if line.startswith(user_username):
            #Stripping and Splitting the sentances so that they can be printed separately.
                temp = line.strip
                temp = line.split(",")

                #Assiging all of the sentances to variables so they can be used.
                task_name = str(temp[1])
                task_owner = str(temp[0])
                task_date_assigned = str(temp[3])
                task_due_date = str(temp [4])
                task_state = str(temp[-1])
                task_desc = str(temp[2])

                #Removing all of the stuff that exists as it is a list.
                task_name=task_name.replace("[","")
                task_name=task_name.replace("]","")
                task_name=task_name.replace("'","")
                task_name=task_name.replace(",","")

                task_owner=task_owner.replace("[","")
                task_owner=task_owner.replace("]","")
                task_owner=task_owner.replace("'","")
                task_owner=task_owner.replace(",","")

                task_desc=task_desc.replace("[","")
                task_desc=task_desc.replace("]","")
                task_desc=task_desc.replace("'","")
                task_desc=task_desc.replace(",","")

                task_date_assigned=task_date_assigned.replace("[","")
                task_date_assigned=task_date_assigned.replace("]","")
                task_date_assigned=task_date_assigned.replace("'","")
                task_date_assigned=task_date_assigned.replace(",","")

                task_due_date=task_due_date.replace("[","")
                task_due_date=task_due_date.replace("]","")
                task_due_date=task_due_date.replace("'","")
                task_due_date=task_due_date.replace(",","")

                task_state=task_state.replace("[","")
                task_state=task_state.replace("]","")
                task_state=task_state.replace("'","")
                task_state=task_state.replace(",","")

                #Printing all of the tasks in Output 2 method as requested.
                print("___________________________________________________________")
                print("")
                print ("Task:            ",task_name)
                print ("Assigned to:      ",task_owner)
                print ("Date assigned:   ",task_date_assigned)
                print ("Due date:        ",task_due_date)
                print ("Task Complete?:  ",task_state)
                print("Task description:")
                print(task_desc)
                print("___________________________________________________________")
                
 elif menu == 'e':
        print('Goodbye!!!')
        exit()

 else:
    print("You have made a wrong choice, Please Try again")
