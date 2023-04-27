#Getting variables and displaying them to the user for clarity.
print("")
#Using float casting as int would only allow whole numbers for the minutes.
swimming_time=float(input("Please enter your swimming time (minutes): "))
print("")
print("You finished swimming with a time of:",swimming_time,"minutes.")
print("")

cycling_time=float(input("Please enter your cycling time (minutes): "))
print("")
print("You finished cycling with a time of:",cycling_time,"minutes.")
print("")

running_time=float(input("Please enter your running time (minutes): "))
print("")
print("You finished running with a time of:",running_time,"minutes.")
print("")

#Adding times together in order to give total. Rounding to 2 decimal places for clarity.
total_time=round((swimming_time+cycling_time+running_time),2)
print("The total time it took for you to finish your triathlon is:",total_time,"minutes")
print("")

#Using if and elif statements to display which award the user has gotten. 
if total_time<=100:
    print("Congratulations! You are within 100 minutes, therefore you have been awarded your Provincial Colours!")
    print("")

#Using 100.01 as any time that is this or over would fit in this boundary.
elif total_time<= 105 and total_time>=100.01:
    print("Congratulations! You have earned provincial Half Colours! Well done!")
    print("")

elif total_time <=110 and total_time>=105.01:
    print("Congratulations! You are within 10 minutes of qualifying time therefore you have earned a Provincial Scroll! Well done!")
    print("")

#There are no other options, therefore else can be used here. 
else:
    print("Unfortunately you have not earned an award as you are more than 10 minutes outside of qualifying time. Better luck next time!")
    print("")