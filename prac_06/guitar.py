class Guitar:
    def __init__(self, name = "", year = 0, cost = 0):
        self.name = name
        self.year = year
        self.cost = cost
    
    def __str__(self):
        return f"{self.name: <20s} ({f'{self.year:d}':>4s}), worth $ {self.cost:,.2f}"
    
    def get_age(self):
        return 2020 - self.year
    
    def is_vintage(self):
        return self.get_age() >= 50