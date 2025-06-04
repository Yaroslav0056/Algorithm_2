import unittest
from src.avl_priority_queue import Tree


class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.insert(10, 3)
        self.tree.insert(20, 1)
        self.tree.insert(30, 4)
        self.tree.insert(40, 2)

    def test_insert(self):
        values = []

        def collect_values(node):
            if node:
                collect_values(node.left)
                values.append((node.value, node.priority))
                collect_values(node.right)

        collect_values(self.tree.root)
        self.assertEqual(values, [(20, 1), (40, 2), (10, 3), (30, 4)])

    def test_pop(self):
        min_value = self.tree.pop()
        self.assertEqual(min_value, 20)
        values = []

        def collect_values(node):
            if node:
                collect_values(node.left)
                values.append((node.value, node.priority))
                collect_values(node.right)

        collect_values(self.tree.root)
        self.assertEqual(values, [(40, 2), (10, 3), (30, 4)])

    def test_empty_pop(self):
        empty_tree = Tree()
        min_value = empty_tree.pop()
        self.assertIsNone(min_value)

    def test_inorder(self):
        values = []

        def collect_values(node):
            if node:
                collect_values(node.left)
                values.append((node.value, node.priority))
                collect_values(node.right)

        collect_values(self.tree.root)
        self.assertEqual(values, [(20, 1), (40, 2), (10, 3), (30, 4)])


if __name__ == "__main__":
    unittest.main()
