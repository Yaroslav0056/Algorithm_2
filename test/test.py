import unittest
from src.lab_8 import calculate_minimal_length


class TestIoTtelecom(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(calculate_minimal_length("communication_wells.csv"), 6000)

    def test_abnormal_case(self):
        self.assertEqual(
            calculate_minimal_length("communication_wells_no_connect.csv"), -1
        )

    def test_empty_case(self):
        self.assertEqual(calculate_minimal_length("communication_wells_empty.csv"), -1)

    def test_big_case(self):
        self.assertEqual(calculate_minimal_length("communication_wells_big.csv"), 9000)
