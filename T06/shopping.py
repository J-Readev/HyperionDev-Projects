#For this task I will need to get a products list from the user, and then get the price of those products.
#I start this off by using the input function to get the product names and assigning them to a variable.
print("")
print("Hello there! I am going to ask you a few things about three of your shopping list products.")
print("")
print("To start with, please can you answer the following questions:")
print("")
product_1=(input("Please name your first product: "))
print("")
product_2=(input("Please name your second product: "))
print("")
product_3=(input("Please name your third product: "))
print("")
print("Thank you! Now I will need the prices of your items,to two decimal places.")
print("")
#Now I have the actual products I will need to gather the prices.
#I do this by using the input function again to assign the product price variables.
#I ask the user for the price and assign it a variable.
#I use the product variables made earlier in order to let the user know which product I am asking about.
#I also use the fload function in order to change this from a string to a float so I can use the inputs in calculations.
product_1_price=(float(input("Please enter the price of" + " " +product_1+": £")))
print("")
product_2_price=(float(input("Please enter the price of" + " " +product_2+": £")))
print("")
product_3_price=(float(input("Please enter the price of" + " " +product_3+": £")))
print("")
#Now I have the prices of the products.
#I display this to the user so they can see what is input.
print("Your prices are", "£",product_1_price,"£",product_2_price,"and","£",product_3_price)
print("")
#I will now need to calculate the total of all products.
#I do this by assiging a new variable and sum all of the products together.
#I am using the round() function because in testing for some reason I had decimal places go on past two.
#At this stage I am unsure as to why that happened, therefore the round() function should stop it going passed two decimal places.
#This is because I specified the ",2".
product_price_sum=(round((product_1_price+product_2_price+product_3_price),2))
#Now I need to calculate the average price of the products.
#To do this I will need to use the sum of the products and divide it by three to work out the average.
#To do this I will use the round() function to make sure that it is limited to two decimal points, like I did earlier.
#This has now been assigned a variable so I can print out the final sentance needed for the task.
#I work out the average price and assign it a variable.
#I then assign the rounded price a variable as well to be able to diplay it to the user.
average_product_price=(product_price_sum/3)
rounded_product_price_sum=(round(average_product_price,2))
print("The total cost of",product_1,",",product_2,"and",product_3,"is £",product_price_sum,"and the average price of the items is £",rounded_product_price_sum)
print("")