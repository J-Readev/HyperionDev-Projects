print("")

#Assigning all needed variables.
air_travel=0.36

freight_travel=0.25

full_insurance=50.00

ltd_insurance=25.00

gift_package=15.00

not_gift_package=0.00

priority_delivery=100.00

standard_delivery=20.00


#Getting user input.
package_price=float(input("Please enter the price of the package you would like to purchase: R "))

print("")

print("Thank you, you have chosen a price of R", package_price)

print("")

#Assigning as a float as most likely using decimals for km & money.
package_delivery_distance=float(input("Please enter the total distance of the delivery in kilometers: "))

print("")

print("Thank you, you have chosen a delivery distance of:", package_delivery_distance,"KMs")

print("")

#Assigning variable to input option.
#Using If statements to check what the user selects, and then calculating the cost based on the users input.
#If the user selects air, it will calculate how much that will cost.
package_delivery_option=input("Do you wish to send this package via air or freight? (air/freight): ")
if package_delivery_option=="air":
    print("")
    print("You have chosen: air")
    cost1=package_delivery_distance*air_travel
    
#If the user selects anything else, this will calculate how much freight travel will cost.
    print("")
else:
    print("")
    print("You have chosen: Freight")
    print("")
    cost1=package_delivery_distance*freight_travel
    
#Same again, getting input.
insurance_option=input("Do you wish to send this package with full insurance or limited insurance? (full/ltd): ")
print("")
#Using if function to check for the user selecting full insurance, if selected it will be added on.
if insurance_option=="full":
    print("You have chosen: full Insurance")
    print("")
    cost2=cost1+full_insurance

#If anything else, limited insurance will be selected. 
else:
    print("You have chosen: limited Insurance")   
    print("") 
    cost2=cost1+ltd_insurance
    

gift_option=input("Is this package a gift? (yes/no): ")
print("")
if gift_option=="yes":
    print("You have chosen to have this package gift wrapped.")
    print("")
    cost3=cost2+gift_package
    
else:
    print("You have chosen not to gift wrap this package.")
    print("")  
    cost3=cost2+not_gift_package
    
#As I am going along, I am running a calculation to see what the current cost is.
#This can be seen by cost1, cost2, cost 3 etc.
priority_option=input("Do you wish to send this package with priority? (yes/no) ")
print("")
if gift_option=="yes":
    print("You have chosen to have this package sent with priority.")
    print("")
    cost4=cost3+priority_delivery
   
else:
    print("You have chosen standard delivery.")
    print("")  
    cost4=cost3+standard_delivery

#I now add the package price to cost 4 in order to determine the final price of the package.
#I print that for the user to see.
final_price=cost4+package_price
print("Thank you for filling your details in. The cost to send your package with the information you have given is: R",final_price)
print("")
