#Printing numbers 1 to 1000.

#This will print every character from 1 up to 1000 because of the for loop adding 1 untill it reaches the end of the range.
for x in range (0,1000):
    print(x+1)
    
#This will print every number that is even in the same way. 
#If statement checks if it is even and only prints it if so. All odd numbers are excluded.
for x in range (0,1000):
    if (x+1)%2==0:
        print(x+1)
