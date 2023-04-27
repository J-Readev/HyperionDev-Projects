#This is a program to calculate someones BMI by getting the users input and calculating what it will be.

print("")

#Getting user weight & height. Floats as need to convert to decimals.
user_weight=float(input("Please provide your weight in kilograms: "))
print("")
print("You have entered", user_weight, "kg")
print("")

user_height=float(input("Please provide your height in metres: "))
print("")
print("You have entered", user_height, "m")

#Setting variable for BMI calculation. Rounding so that it is a number to the 2nd decimal point.
bmi_calc=round((user_weight)/((user_height*user_height)),2)

print("")
print("From what you have entered, your BMI is roughly:",bmi_calc)
print("")

#If statements to determine if user is obese, overweight, normal or underweight.
#Above 30 = obese.
if bmi_calc >=30:
    print("Your BMI indicates that you may be obese.")
    print("")

#Elif to see if BMI is more than or equal to 25 or 29 or less = overweight.
elif bmi_calc >=25 and bmi_calc <=29:
    print("Your BMI indicates you may be overweight.")
    print("")

#Elif to see if weight is normal (between or equal to 18.5 and 24)
elif bmi_calc >=18.5 and bmi_calc <=24:
    print("Your BMI indicates your weight is considered normal.")
    print("")

#Else statement as all other options the user could input would calculate to be underweight.
else:
    print("Your BMI indicates you are underweight.")
    print("")