#Creating list to add friends. 
friend_list = ["Dave Bongo", "Wade Smith","Brian Dingle"]
print("")

#Printing first friend, 0 is the first list item.
print("My first friend in my list is:",friend_list[0])
print("")

#Priting last friend, -1 is the last list item no matter how long the list.
#I could have used 2 but that only works because I know how many names are in the list.
print("My last friend in my list is:",friend_list[-1])
print("")

#This is to print the amount of items in the list, using len. 
print("The amount of friends I have on my list is:",len(friend_list))
print("")

#List for friends ages.
friends_ages = [34, 31, 78]

#Printing for user.
print(friend_list[0],"is",friends_ages[0])
print("")
print(friend_list[1],"is",friends_ages[1])
print("")
print(friend_list[-1],"is",friends_ages[-1])
print("")