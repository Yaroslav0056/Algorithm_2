import unittest
from src.lab_6 import smart_minimum_beers


class TestBeerSelection(unittest.TestCase):
    def test_minimal_case(self):
        self.assertEqual(smart_minimum_beers(1, 1, "Y"), 1)

    def test_unique_preferences(self):
        self.assertEqual(smart_minimum_beers(3, 3, "YNNNYNNNY"), 3)

    def test_all_like_same(self):
        self.assertEqual(smart_minimum_beers(4, 2, "YNYNYNYN"), 1)

    def test_from_task(self):
        self.assertEqual(smart_minimum_beers(6, 3, "YNNYNYYNYNYYNYYNYN"), 2)

    def test_partial_overlap(self):
        self.assertEqual(smart_minimum_beers(4, 3, "YNNYNYNYNNNY"), 3)

    def test_another_overlap(self):
        self.assertEqual(smart_minimum_beers(5, 3, "YNNYNYYNNYNYNYY"), 2)


if __name__ == "__main__":
    unittest.main()
