# flight trip class
class FlightTrip:
    def __init__(self, origin, destination, plane_number):
        self.origin = origin
        self.destination = destination
        self.plane_number = plane_number
        self.list_of_passengers = []

    def add_to_passengers(self, passenger_input):
        self.list_of_passengers.append(passenger_input)





# origin
# destination
# list_of_passengers
# plane_number

# use encapsulation (use getters and setters)