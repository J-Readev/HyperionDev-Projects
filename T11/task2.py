import math
#I will need math in this task in order to use pi for the area of a circle.

#Getting input.
print("")
building_shape=input("What is the shape of your building? (square, rectangle or round): " )

#Using if to check if the building is square. If it is, it runs the below code which calculates the area of the square.
if building_shape==("square"):
    print("")
    print("The shape you have chosen is a is a square.")
    print("")
    #Float for decimals.
    building_length=float(input("What is the length of your building? (Metres) :"))
    print("")
    #Rounding to 2 decimal places in order to look better. ** to make this to the power of 2.
    building_area=round((building_length**2),2)
    print("")
    #Printing for user to see.
    print("The area of your building to two decimal points is: ",building_area,"metres squared.")
    print("")

#Elif to check if user has inputted rectangle. Runs the below code.
elif building_shape==("rectangle"):
    print("")
    print("The shape you have chosen is a rectangle.")
    print("")
    building_length=float(input("What is the length of your building? (Metres) :"))
    print("")
    building_width=float(input("What is the width of your building? (Metres) :"))
    print("")
    building_area=round((building_width*building_length),2)
    print("")
    print("The area of your building to two decimal points is: ",building_area,"metres squared.")
    print("")

#Else for all other options as the only option that is not covered by if and elif is round, for a circle.
else:
    print("")
    print("The shape you have chosen is round, so it will be a calculated as a circle.")
    print("")
    building_radius=float(input("What is the radius of your building? (Metres) :"))
    print("")
    #Imported math earlier, so math.pi could be used to calculate area of a circle.
    building_area=round(math.pi*(building_radius**2),2)
    print("The area of your building to two decimal points is: ",building_area,"metres squared.")
    print("")
