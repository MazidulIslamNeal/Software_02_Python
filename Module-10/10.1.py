class Elevator:
    def __init__(self, bottom_floor_num, top_floor_num):
        self.bottom_floor_num = bottom_floor_num
        self.top_floor_num = top_floor_num
        self.current = bottom_floor_num

    def go_to_floor(self, floor_to_go):
        while self.current < floor_to_go:
            self.floor_up()

        while self.current > floor_to_go:
            self.floor_down()

    def floor_up(self):
        self.current += 1
        print(f"You are in floor number {self.current} now!")


    def floor_down(self):
        self.current -= 1
        print(f"You are in floor number {self.current} now!")


h = Elevator(0,10)

h.go_to_floor(5)
h.go_to_floor(10)
h.go_to_floor(9)
h.go_to_floor(2)
h.go_to_floor(8)
