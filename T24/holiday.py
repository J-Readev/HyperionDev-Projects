
#Defining function that can determine the cost of the hotel stay.
def hotel_cost(days_spent):
    daily_rate = 50
    total = daily_rate * days_spent
    return total

#Plane Cost function.

def plane_cost(arrival_city):
    if arrival_city == "Birmingham":
        cost = 200
    elif arrival_city == "Nottingham":
        cost= 150
    elif arrival_city == "Banbury":
        cost = 100
    else:
        cost = "The plane does not fly here. Try again!"
    
    return cost

#Car Rental function.

def car_rental(days_hired):
    car_daily_rate = 10
    car_total = car_daily_rate * days_hired
    return car_total

#Creating function which determines the cost of the entire trip, using the previously defined functions inside of it.
def holiday_cost(x, y, z):
    cost_1 = hotel_cost(x)
    cost_2 = plane_cost(y)
    cost_3 = car_rental(z)

    total_cost = cost_1 + cost_2 + cost_3

    return total_cost

#Getting user input in order to determine costs.
x = int(input("Please state how many days you wish to stay in a hotel for: "))
print("Your hotel stay will cost: £",hotel_cost(x))

print("")
y = input("Please select the city you wish to arrive at (Birmingham, Nottingham or Banbury): ")
print("Your flight will cost: £", plane_cost(y))

print("")
z = int(input("Please state how many days you wish to hire the car for: "))
print("Your rental car will cost: £", car_rental(z))

#Variables are determined, so can input them into the holiday cost function which has been pre-defined and displaying for user.
print("")
print("The total cost of your holiday is: £",holiday_cost(x,y,z))