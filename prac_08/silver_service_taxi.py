from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = fanciness*Taxi.price_per_km
    def drive(self, distance):
        super().drive(distance)
    def get_fare(self):
        return super().get_fare() + self.flagfall
    def start_fare(self):
        super().start_fare()
    def __str__(self):
        return f"{super().__str__()}, {self.current_far_distance}, on current fare: ${self.price_per_km:.2d}/km plus flagfall of ${self.flagfall}"
