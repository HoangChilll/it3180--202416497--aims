import io
import unittest
from contextlib import redirect_stdout

from aims.cart import Cart
from aims.dvd import DVD


class CartTests(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for index in range(20):
            self.assertTrue(cart.add_dvd(DVD(str(index), 1)))
        self.assertFalse(cart.add_dvd(DVD("extra", 1)))
        self.assertEqual(20, len(cart.items))

    def test_total_cost(self):
        cart = Cart()
        cart.add_dvd(DVD("A", 10.0))
        cart.add_dvd(DVD("B", 2.5))
        self.assertEqual(12.5, cart.total_cost())

    def test_print_empty_cart(self):
        output = io.StringIO()
        with redirect_stdout(output):
            Cart().print_cart()
        self.assertEqual("The cart is empty\n", output.getvalue())

    def test_add_dvd_on_legacy_console(self):
        cart = Cart()
        output = io.BytesIO()
        console = io.TextIOWrapper(output, encoding="cp1252")
        with redirect_stdout(console):
            self.assertTrue(cart.add_dvd(DVD("A", 1)))
        console.flush()
        self.assertIn(b"DVD added to cart", output.getvalue())

    def test_discounted_total(self):
        cart = Cart()
        cart.add_dvd(DVD("A", 100))
        self.assertEqual(80, cart.total_cost_with_discount(20))

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            Cart().total_cost_with_discount(150)

    def test_sort_by_title(self):
        cart = Cart()
        cart.items = [DVD("Zulu", 2), DVD("alpha", 1)]
        cart.sort_by_title()
        self.assertEqual(["alpha", "Zulu"], [dvd.title for dvd in cart.items])

    def test_sort_by_cost(self):
        cart = Cart()
        cart.items = [DVD("A", 3), DVD("B", 1)]
        cart.sort_by_cost()
        self.assertEqual(["B", "A"], [dvd.title for dvd in cart.items])
