class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        self.items.append(dvd)

    def total_cost(self):
        return sum(dvd.price for dvd in self.items)

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return
        for index, dvd in enumerate(self.items, start=1):
            print(f"{index}. {dvd.title}: {dvd.price:.2f} $")
