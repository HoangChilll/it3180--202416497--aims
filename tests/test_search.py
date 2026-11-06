import unittest

from aims.dvd import DVD
from aims.search import search_by_title


class SearchTests(unittest.TestCase):
    def test_search_by_title(self):
        discs = [DVD("The Lion King", 19.99), DVD("Star Wars", 24.99)]
        self.assertEqual([discs[0]], search_by_title(discs, "Lion"))

    def test_search_by_title_ignores_case(self):
        discs = [DVD("The Lion King", 19.99)]
        self.assertEqual(discs, search_by_title(discs, "lion"))
