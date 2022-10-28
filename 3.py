class human:
    def __init__(self, name = "human"):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []

    def addpassanger(self, human):
        self.passenger.append(human)

    def print_passangers_name(self):
        if self.passenger != []:
            print(f"Names {self.brand} passenger")
            for passenger in self.passenger:
                print(passenger.name)
            else:
                print(f"no passenger in {self.brand}")
hum1 = human("Jamal")
hum2 = human("Jack")

auto1 = Auto("MERCEDES")
auto2 = Auto("BEMEWE")
auto2.print_passangers_name()
auto1.print_passangers_name()

auto1.addpassanger(hum1)
auto2.addpassanger(hum2)
auto2.print_passangers_name()
auto1.print_passangers_name()