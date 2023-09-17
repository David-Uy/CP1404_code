from taxi import Taxi

# Create a new taxi object
my_taxi = Taxi("Prius 1", 100, 1.23)

# Drive the taxi 40 km
distance_driven = my_taxi.drive(40)


# Print the taxi's details and the current fare
print(my_taxi)

# Restart the meter (start a new fare) and then drive the car 100 km
my_taxi.start_fare()
distance_driven = my_taxi.drive(100)

# Print the details and the current fare
print(my_taxi)
