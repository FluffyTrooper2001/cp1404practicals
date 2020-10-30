from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50
    def __init__(self, fuel, name, fanciness):
        super().__init__(fuel=fuel,name=name)
        self.price_per_km = fanciness*Taxi.price_per_km
    def drive(self, distance):
        return super().drive(distance)
    def get_fare(self):
        return super().get_fare() + self.flagfall
    def start_fare(self):
        super().start_fare()
    def __str__(self):
        return f"{super().__str__()}, plus flagfall of ${self.flagfall}"
