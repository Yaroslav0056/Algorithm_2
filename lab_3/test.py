import unittest
from lab_3 import BinaryTree, is_tree_balanced


class TestTreeBalance(unittest.TestCase):
    def test_balanced_tree(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        self.assertTrue(is_tree_balanced(root))

    def test_unbalanced_tree(self):
        root2 = BinaryTree(1)
        root2.left = BinaryTree(2)
        root2.left.left = BinaryTree(3)
        root2.left.left.left = BinaryTree(4)
        root2.right = BinaryTree(8)
        self.assertFalse(is_tree_balanced(root2))

    def test_single_node_tree(self):
        root = BinaryTree(1)
        self.assertTrue(is_tree_balanced(root))


if __name__ == "__main__":
    unittest.main()
