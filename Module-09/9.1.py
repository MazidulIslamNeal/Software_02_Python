class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

# Creating a new car
new_car = Car("ABC-123", 142)

# Printing out all the properties of the new car
print(f"Registration Number: {new_car.registration_number}")
print(f"Maximum Speed: {new_car.max_speed} km/h")
print(f"Current Speed: {new_car.current_speed} km/h")
print(f"Travelled Distance: {new_car.travelled_distance} km")
