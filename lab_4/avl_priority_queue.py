class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if node:
        return node.height
    return 0

def get_balance(node):
    if node:
        return get_height(node.left) - get_height(node.right)
    return 0

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def insert(node, value, priority):
    if not node:
        return Node(value, priority)

    if priority <= node.priority:
        node.left = insert(node.left, value, priority)
    else:
        node.right = insert(node.right, value, priority)

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    if balance > 1 and priority <= node.left.priority:
        return right_rotate(node)
    if balance < -1 and priority > node.right.priority:
        return left_rotate(node)
    if balance > 1 and priority > node.left.priority:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if balance < -1 and priority <= node.right.priority:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def get_min_priority(node):
    while node.left:
        node = node.left
    return node

def remove_min(node):
    if not node.left:
        return node.right
    node.left = remove_min(node.left)
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    if balance > 1:
        if get_balance(node.left) >= 0:
            return right_rotate(node)
        else:
            node.left = left_rotate(node.left)
            return right_rotate(node)

    if balance < -1:
        if get_balance(node.right) <= 0:
            return left_rotate(node)
        else:
            node.right = right_rotate(node.right)
            return left_rotate(node)

    return node

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        self.root = insert(self.root, value, priority)

    def pop(self):
        if not self.root:
            return None
        min_node = get_min_priority(self.root)
        self.root = remove_min(self.root)
        return min_node.value

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"id: {node.id}, залишок: {node.quantity}")
            self.inorder(node.right)
        else:
            return None
tree = Tree()
tree.insert(10, 3)
tree.insert(20, 1)
tree.insert(30, 4)
tree.insert(40, 2)
tree.pop()
tree.pop()
tree.pop()
tree.pop()

tree.inorder(tree.root)
