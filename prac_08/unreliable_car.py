from car import Car 

import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        assert reliability <= 100 and reliability >= 0
        self.reliability = reliability
    def drive(self, distance):
        rand_num = random.randint(0,100)
        if rand_num < self.reliability:
            return super().drive(distance)
        else:
            return 0
    def __str__(self):
        return f"{super().__str__()}, reliability {self.reliability}"
