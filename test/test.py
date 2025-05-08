import unittest
from src.lab_7 import kmp_search


class TestKMPSearch(unittest.TestCase):

    def test_multiple_occurrences(self):
        self.assertEqual(kmp_search("лілі", "лілілось лілілось"), [(0, 3), (9, 12)])

    def test_single_occurrence(self):
        self.assertEqual(kmp_search("ліліло", "лілілось лілілось"), [(0, 5), (9, 14)])

    def test_no_match(self):
        self.assertEqual(
            kmp_search("ліліла", "лілілось лілілось"), "Підстроку не знайдено"
        )

    def test_partial_match_only(self):
        self.assertEqual(kmp_search("лох", "лілілохсь лілілохсь"), [(4, 6), (14, 16)])

    def test_empty_needle(self):
        self.assertEqual(kmp_search("", "щось"), [])

    def test_empty_haystack(self):
        self.assertEqual(kmp_search("abc", ""), [])

    def test_both_empty(self):
        self.assertEqual(kmp_search("", ""), [])

    def test_overlap_matches(self):
        self.assertEqual(kmp_search("aaa", "aaaaaa"), [(0, 2), (1, 3), (2, 4), (3, 5)])


if __name__ == "__main__":
    unittest.main()
