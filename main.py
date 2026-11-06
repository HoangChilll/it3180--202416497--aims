from aims.cart import Cart
from aims.dvd import DVD


def main():
    cart = Cart()
    cart.add_dvd(DVD("The Lion King", 19.99))
    cart.add_dvd(DVD("Star Wars", 24.99))
    cart.add_dvd(DVD("Aladdin", 18.91))
    print(f"Total cost: {cart.total_cost():.2f} $")


if __name__ == "__main__":
    main()
