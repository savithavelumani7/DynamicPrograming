class Taxi:
    def __init__(self, id):
        self.id = id
        self.location = 'A'
        self.earnings = 0
        self.is_free = True

    def move_to(self, location):
        self.location = location

    def update_earnings(self, distance):
        self.earnings += 100 + (distance - 5) * 10 if distance > 5 else 100

class TaxiBookingSystem:
    def __init__(self):
        self.taxis = [Taxi(i) for i in range(1, 5)]
        self.points = {'A': 0, 'B': 15, 'C': 30, 'D': 45, 'E': 60, 'F': 75}

    def calculate_distance(self, point1, point2):
        return abs(self.points[point1] - self.points[point2])

    def find_nearest_taxi(self, pickup_point):
        free_taxis = [taxi for taxi in self.taxis if taxi.is_free]
        if not free_taxis:
            return None

        free_taxis.sort(key=lambda taxi: (self.calculate_distance(taxi.location, pickup_point), taxi.earnings))
        return free_taxis[0]

    def book_taxi(self, pickup_point, drop_point):
        nearest_taxi = self.find_nearest_taxi(pickup_point)
        if nearest_taxi:
            nearest_taxi.is_free = False
            travel_distance = self.calculate_distance(pickup_point, drop_point)
            nearest_taxi.update_earnings(travel_distance)
            nearest_taxi.move_to(drop_point)
            nearest_taxi.is_free = True  # Assume taxi becomes free immediately after drop
            print(f"Taxi {nearest_taxi.id} booked from {pickup_point} to {drop_point}. Earnings: Rs.{nearest_taxi.earnings}")
        else:
            print("No taxis available. Booking rejected.")

# Test the system
booking_system = TaxiBookingSystem()

# Test bookings
booking_system.book_taxi('A', 'B')
booking_system.book_taxi('A', 'C')
booking_system.book_taxi('B', 'D')
booking_system.book_taxi('A', 'E')
booking_system.book_taxi('C', 'F')
