import unittest
from lab_5 import bfs


class TestBFS(unittest.TestCase):

    def test_start_equals_end(self):
        dist, _ = bfs(8, (4, 4), (4, 4))
        self.assertEqual(dist, 0)

    def test_direct_move(self):
        dist, _ = bfs(8, (0, 0), (2, 1))
        self.assertEqual(dist, 1)

    def test_reachable_far(self):
        dist, _ = bfs(8, (0, 0), (7, 7))
        self.assertEqual(dist, 6)

    def test_unreachable_small_board(self):
        dist, _ = bfs(2, (0, 0), (1, 1))
        self.assertEqual(dist, -1)


if __name__ == "__main__":
    unittest.main()
