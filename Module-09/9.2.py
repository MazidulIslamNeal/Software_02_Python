class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        self.current_speed = max(0, min(new_speed, self.max_speed))

# Creating a new car
new_car = Car("ABC-123", 142)

# Accelerating the car
speed_changes = [30, 70, 50]

for change in speed_changes:
    new_car.accelerate(change)

# Printing out the current speed of the car
print(f"Current Speed: {new_car.current_speed} km/h")

# Applying emergency brake
new_car.accelerate(-200)

# Printing out the final speed after applying the emergency brake
print(f"Final Speed: {new_car.current_speed} km/h")
