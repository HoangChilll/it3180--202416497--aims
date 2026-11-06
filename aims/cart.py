class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        self.items.append(dvd)

    def total_cost(self):
        return sum(dvd.price for dvd in self.items)
