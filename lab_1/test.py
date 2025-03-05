import unittest
from FUS import find_unsorted_subarray

class TestFindUnsortedSubarray(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(find_unsorted_subarray([1, 2, 3, 4, 5]), (-1, -1))

    def test_single_element(self):
        self.assertEqual(find_unsorted_subarray([1]), (-1, -1))

    def test_completely_unsorted(self):
        self.assertEqual(find_unsorted_subarray([5, 4, 3, 2, 1]), (0, 4))

    def test_partially_unsorted(self):
        self.assertEqual(find_unsorted_subarray([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), (3, 9))

    def test_edge_case(self):
        self.assertEqual(find_unsorted_subarray([2, 6, 4, 8, 10, 9, 15]), (1, 5))


if __name__ == '__main__':
    unittest.main()