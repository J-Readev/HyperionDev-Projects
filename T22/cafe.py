
#Creating Menu List.
menu = ["Americano","Tea","Mocha","Latte"]

#Creating Stock Dictionary.
stock = {"Americano": 10,
"Tea":15,
"Mocha":5,
"Latte":20
}

#Creating Price Dictionary.
price = {"Americano": 2.50,
"Tea":1.50,
"Mocha":3,
"Latte":3.50
}

#Using a for loop to calculate each parts of the dictonary multiplied together, then adding them together.
total_value = 0
for key in price:
    key = (price[key] * stock [key])
    total_value = key + total_value

print("")
print("The total value of the stock is: £",total_value)
print("")

    
#Americano: 25
#Tea: 22.5
#Mocha: 15
#Latte: 70

#Final cost should be £132.5.






