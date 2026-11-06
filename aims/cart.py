MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        print(f"Đã thêm đĩa '{dvd.title}' vào giỏ hàng")
        return True

    def total_cost(self):
        return sum(dvd.price for dvd in self.items)

    def total_cost_with_discount(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        return self.total_cost() * (1 - percent / 100)

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return
        for index, dvd in enumerate(self.items, start=1):
            print(f"{index}. {dvd.title}: {dvd.price:.2f} $")
