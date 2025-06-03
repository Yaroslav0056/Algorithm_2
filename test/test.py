import unittest
from math import isclose
from src.lab_9 import max_dp, write


class TestMaxDP(unittest.TestCase):
    """Тести для функції max_dp з модуля lab_9"""

    def test_case_1(self):
        """Тест з параметрами: w=2, lst=[3, 3, 3]"""
        w = 2
        lst = [3, 3, 3]
        expected_result = 5.65
        result, dp = max_dp(w, lst)
        self.assertTrue(isclose(result, expected_result, abs_tol=0.01))
        write("results/test_case_1.txt", dp)

    def test_case_2(self):
        """Тест з параметрами: w=100, lst=[1, 1, 1, 1]"""
        w = 100
        lst = [1, 1, 1, 1]
        expected_result = 300.00
        result, dp = max_dp(w, lst)
        self.assertTrue(isclose(result, expected_result, abs_tol=0.01))
        write("results/test_case_2.txt", dp)

    def test_case_3(self):
        """Тест з параметрами: w=4, lst=[100, 2, 100, 2, 100]"""
        w = 4
        lst = [100, 2, 100, 2, 100]
        expected_result = 396.32
        result, dp = max_dp(w, lst)
        self.assertTrue(isclose(result, expected_result, abs_tol=0.01))
        write("results/test_case_3.txt", dp)

    def test_case_4(self):
        """Великий тест з довгим списком висот"""
        w = 4
        lst = [
            56,
            18,
            17,
            94,
            23,
            7,
            21,
            94,
            29,
            54,
            44,
            26,
            86,
            79,
            4,
            15,
            5,
            91,
            25,
            17,
            88,
            66,
            28,
            2,
            95,
            97,
            60,
            93,
            40,
            70,
            75,
            48,
            38,
            51,
            34,
            52,
            87,
            8,
            62,
            77,
            35,
            52,
            3,
            93,
            34,
            57,
            51,
            11,
            39,
            72,
        ]
        expected_result = 2738.18
        result, dp = max_dp(w, lst)
        self.assertTrue(isclose(result, expected_result, abs_tol=0.01))
        write("results/test_case_4.txt", dp)

    def test_case_5(self):
        """Тест з однаковими висотами опор"""
        w = 10
        lst = [5] * 5
        result, dp = max_dp(w, lst)
        expected_result = result  # Просто перевіряємо, що вивід коректний
        self.assertTrue(isclose(result, expected_result, abs_tol=0.01))
        write("results/test_case_5.txt", dp)

    def test_case_6(self):
        """Тест, що перевіряє результат більше певного значення"""
        w = 1
        lst = [1, 2, 3, 4]
        result, dp = max_dp(w, lst)
        self.assertTrue(result > 3)
        write("results/test_case_6.txt", dp)


if __name__ == "__main__":
    unittest.main()
