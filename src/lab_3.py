class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_height(node):
    if not node:
        return 0

    left_height = get_height(node.left)
    if left_height == -1:
        return -1

    right_height = get_height(node.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1


def is_tree_balanced(root):
    return get_height(root) != -1


# Збалансоване дерево
root1 = BinaryTree(3)
root1.left = BinaryTree(9)
root1.right = BinaryTree(20)

# Незбалансоване дерево
root2 = BinaryTree(1)
root2.left = BinaryTree(2)
root2.left.left = BinaryTree(3)
root2.left.left.left = BinaryTree(4)
root2.right = BinaryTree(8)

print(is_tree_balanced(root1))
print(is_tree_balanced(root2))
