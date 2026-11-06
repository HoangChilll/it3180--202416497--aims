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
