import unittest
from src.lab_2 import min_board


class TestMinBoardSize(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(min_board(10, 2, 3), 9)
        self.assertEqual(min_board(2, 1000000000, 999999999), 1999999998)

    def test_small_cases(self):
        self.assertEqual(min_board(2, 1, 1), 2)

    def test_large_cases(self):
        self.assertEqual(min_board(100000, 1000, 1000), 317000)


if __name__ == "__main__":
    unittest.main()
