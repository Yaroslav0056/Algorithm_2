import unittest
from src.lab_8 import calculate_minimal_length


class TestIoTtelecom(unittest.TestCase):
    def test_normal_case(self):
        print("test_normal_case:")
        self.assertEqual(
            calculate_minimal_length("../data_test/communication_wells.csv"), 6000
        )

    def test_abnormal_case(self):
        print("test_abnormal_case:")
        self.assertEqual(
            calculate_minimal_length("../data_test/communication_wells_no_connect.csv"),
            -1,
        )

    def test_empty_case(self):
        print("test_empty_case:")
        self.assertEqual(
            calculate_minimal_length("../data_test/communication_wells_empty.csv"), -1
        )

    def test_big_case(self):
        print("test_big_case:")
        self.assertEqual(
            calculate_minimal_length("../data_test/communication_wells_big.csv"), 9000
        )
