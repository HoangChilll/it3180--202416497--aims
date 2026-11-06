from aims.cart import Cart
from aims.dvd import DVD
from aims.search import search_by_title
from aims import __version__


def main():
    print(f"AIMS-mini v{__version__}")
    cart = Cart()
    cart.add_dvd(DVD("The Lion King", 19.99))
    cart.add_dvd(DVD("Star Wars", 24.99))
    cart.add_dvd(DVD("Aladdin", 18.91))
    print(f"Total cost: {cart.total_cost():.2f} $")
    cart.print_cart()
    print("Search for Lion:", [dvd.title for dvd in search_by_title(cart.items, "Lion")])


if __name__ == "__main__":
    main()
