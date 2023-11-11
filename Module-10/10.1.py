class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor request")
            return

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("Already at the top floor")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("Already at the bottom floor")

# Testing the Elevator class
if __name__ == "__main__":
    # Creating an elevator from the 1st floor to the 10th floor
    elevator = Elevator(bottom_floor=1, top_floor=10)

    # Moving to the 5th floor
    elevator.go_to_floor(5)

    # Moving back to the bottom floor
    elevator.go_to_floor(1)
