import unittest

from aims.dvd import DVD
from aims.search import search_by_category, search_by_title


class SearchTests(unittest.TestCase):
    def test_search_by_category(self):
        discs = [DVD("A", 1, "Family"), DVD("B", 2, "Action")]
        self.assertEqual([discs[0]], search_by_category(discs, "family"))

    def test_search_by_title(self):
        discs = [DVD("The Lion King", 19.99), DVD("Star Wars", 24.99)]
        self.assertEqual([discs[0]], search_by_title(discs, "Lion"))

    def test_search_by_title_ignores_case(self):
        discs = [DVD("The Lion King", 19.99)]
        self.assertEqual(discs, search_by_title(discs, "lion"))
