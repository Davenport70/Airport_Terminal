from People import *
# Passenger class

class Passenger(People):
# inherits from people
    def __init__(self, name, passport_number):
        super().__init__(name)
        self.passport_number = passport_number

passenger1 = Passenger('Joana Thomson', 'B343123')
print(passenger1.name, passenger1.passport_number)
passenger2 = Passenger('Birt Kuman', 'B13927')
print(passenger2.name, passenger2.passport_number)
# attributes:
# passport number