import os
os.system('cls')

total_distance = float(input("What was the total distance? (in km) "))
car_performance = float(input("What was the car performance? (in km/l) "))
gasoline_price = float(input("Which is the current cost of the gas? $"))

total_liters = round(total_distance / car_performance, 2) #Calculated the liters we need for the journey
total_price = round(total_liters * gasoline_price, 2) #Estimate total budget

print(f"To travel {total_distance} km you are going to need {total_liters} liters, with a final cost of ${total_price} MXN") 