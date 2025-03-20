import unittest
from board import min_board_size

class TestMinBoardSize(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(min_board_size(10, 2, 3), 9)
        self.assertEqual(min_board_size(2, 1000000000, 999999999), 1999999998)

    def test_small_cases(self):
        self.assertEqual(min_board_size(2, 1, 1), 2)  # 2 елементи, один ряд

    def test_large_cases(self):
        self.assertEqual(min_board_size(100000, 1000, 1000), 317000)  # Велике значення для N

if __name__ == "__main__":
    unittest.main()
