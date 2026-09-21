# string
destination = input("Where you going ? ")

# string to float
totalDistance = input("Total distance in miles ? ")
totalDistance = float(totalDistance)

# string to float
fuelMPG = input("Car fuel efficiency in miles per gallon ? ")
fuelMPG = float(fuelMPG)

# string to float
gasPricePerGallon = input("Current gas price per gallon ? ")
gasPricePerGallon = float(gasPricePerGallon)

# string to integer
numberOfNights = input("Number of nights ? ")
numberOfNights = int(numberOfNights)

# string to float
avgHotelCost = input("Average hotel cost ? ")
avgHotelCost = float(avgHotelCost)

# string to float
dailyFood = input("Daily food budget ? ")
dailyFood = float(dailyFood)


# -- Start to calculate..
gallonsOfGasNeeded =  totalDistance / fuelMPG
totalGasCost = gallonsOfGasNeeded * gasPricePerGallon
total_hotel_cost = numberOfNights * avgHotelCost
total_food = (numberOfNights + 1) * dailyFood

# Add everything together
grandTotal = totalGasCost + total_hotel_cost + total_food

print ("=== Road Trip Budget Planner ===")
print ("")
print (f"Destination: {destination}")
print (f"Distance: {totalDistance} miles")
print ("")
print ("--- Cost Breakdown ---")
print (f"Gas ({gallonsOfGasNeeded} gal @ ${gasPricePerGallon:.2f}/gal):  ${totalGasCost:.2f}")
print (f"Hotel ({numberOfNights} nights @ ${avgHotelCost:.2f}):    ${total_hotel_cost:.2f}")
print (f"Food ({(numberOfNights + 1)} days @ ${dailyFood:.2f}):        ${dailyFood:.2f}")
print('-' * 20)
print (f"Estimated Total:               ${grandTotal:.2f}")

