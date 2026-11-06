MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        return True

    def total_cost(self):
        return sum(dvd.price for dvd in self.items)

    def total_cost_with_discount(self, percent):
        return self.total_cost() * percent / 100

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return
        for index, dvd in enumerate(self.items, start=1):
            print(f"{index}. {dvd.title}: {dvd.price:.2f} $")
