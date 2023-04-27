import math
print("")
print("Hello There, You will need to select one of the following options:")
print("")
print("Investment - To calculate the amount of interest you'll earn on your investment.")
print("")
print("Bond - To calculate the amount you'll have to pay on a home lone.")
print("")

#Asking user for their choise of bond / investment.
user_choice=input("Please type what you would like to look into: (Investment or Bond): ")

#The task has asked to ensure that no matter how the input was capitalised, it would be accepted if the characters were correct.
#I did some digging into options other than .upper() .lower() and discovered .capitalize existed through "www.flexiple.com".
#Using this, I can ensure that any errors in capitalisation are corrected but still accepted by the code.
corrected_user_choice=user_choice.capitalize()

#Using the converted input, using if statements to let the user know what they have selected.
if corrected_user_choice=="Investment":
    print("")
    print("You have selected: Investment")
    print("")

#Asking user for their deposit amount.
    user_deposit=float(input("Please enter the amount of money you are depositing: £"))
    print("")

    user_interest_rate=float(input("Please enter the interest rate. Please note: You do not need to add the percentage sign: "))
    print("")

    user_investment_years=float(input("Please enter the amount of years you plan on investing for: "))
    print("")

    #Using .capitalize to avoid errors if the user enters the input with different letters capitalised.
    interest=input("Please select whether you would like Simple or Compound interest: ").capitalize()
    print("")
    
    #Starting the if statements if the user selects simple.
    if interest=="Simple":
        #Using the equations in the task to calculate the interest. Using round in order to keep this within two decimal points.
        print(("The total amount once your interest is applied when using Simple interest will be: £"),round(user_deposit*(1+(user_interest_rate/100)*user_investment_years),2))
        print("")
    
    elif interest=="Compound":
        #Equations again used from the task and using round for the same reason above.
        print(("The total amount once your interest is applied when using Compound interest will be: £"),round(user_deposit*math.pow((1+(user_interest_rate/100)),user_investment_years),2))
        print("")

    #Using an else statement so that the user knows when they have chosen the incorrect option.
    else:
        print("You have not selected the correct option. Please type either Simple or Compound.")
        print("")

elif corrected_user_choice=="Bond":
    print("")
    print("You have selected: Bond")
    print("")

    #Using floats as these could be decimal figures.
    present_house_value=float(input("Please enter the present value of your house: £"))
    print("")

    #Using float as the user could have something like 6.5 percent interest which would not be picked up as an int.
    user_interest_rate=float(input("Please enter the annual interest rate. Please note: You do not need to add the percentage sign: "))
    print("")

    bond_repayment_months=float(input("Please enter the amount of months you plan to take in order to repay the bond: "))
    print("")

    #Making the annual interest rate into the monthly rate here, as this will make the equation easier to read.
    monthly_interest_rate=((user_interest_rate/100)/12)

    #Using the equation in the task to calculate the bond repayment amount. Since math was inported I could use "pow" to put something to the power of something.
    bond_repayment_amount=(present_house_value*monthly_interest_rate)/(1-pow((1+monthly_interest_rate),-bond_repayment_months))
    
    #This will now print the repayment amount, rouded to the nearest penny for the user.
    print("Your monthly repayment amount is the following: £",round((bond_repayment_amount),2))
    print("")

#This has been used so that the user can see they have input neither Investment or Bond, so they have selected the wrong option.
else:
    print("")
    print("You have not selected either Investment or Bond. Please choose between the two.")
    print("")