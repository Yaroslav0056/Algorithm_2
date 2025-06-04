import os
from avl_priority_queue import (
    get_min_priority,
    get_balance,
    get_height,
    right_rotate,
    left_rotate,
)


class Node:
    def __init__(self, id, quantity):
        self.id = id
        self.quantity = quantity
        self.left = None
        self.right = None
        self.height = 1


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, id, quantity):
        self.root = self._insert(self.root, id, quantity)

    def _insert(self, node, id, quantity):
        if not node:
            return Node(id, quantity)

        if id < node.id:
            node.left = self._insert(node.left, id, quantity)
        elif id > node.id:
            node.right = self._insert(node.right, id, quantity)
        else:
            node.quantity = quantity

        node.height = 1 + max(get_height(node.left), get_height(node.right))
        balance = get_balance(node)

        if balance > 1:
            if id < node.left.id:
                return right_rotate(node)
            else:
                node.left = left_rotate(node.left)
                return right_rotate(node)

        if balance < -1:
            if id > node.right.id:
                return left_rotate(node)
            else:
                node.right = right_rotate(node.right)
                return left_rotate(node)

        return node

    def find(self, node, id):
        if not node:
            return None
        if id < node.id:
            return self.find(node.left, id)
        elif id > node.id:
            return self.find(node.right, id)
        else:
            return node

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"id: {node.id}, залишок: {node.quantity}")
            self.inorder(node.right)


class Invent:
    def __init__(self):
        self.tree = Tree()

    def insert(self, id, quantity, silent=False):
        self.tree.insert(id, quantity)
        if not silent:
            print(f"Товар з id {id} додано до складу, залишок: {quantity}")

    def delete(self, id):
        if self.find_item(id):
            self.tree.root = self.remove(self.tree.root, id)
            print(f"Товар з id {id} викрали цигани")
        else:
            print(f"Товар з id {id} загубився")

    def remove(self, node, id):
        if not node:
            return None

        if id < node.id:
            node.left = self.remove(node.left, id)
        elif id > node.id:
            node.right = self.remove(node.right, id)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            min_larger_node = get_min_priority(node.right)
            node.id = min_larger_node.id
            node.quantity = min_larger_node.quantity
            node.right = self.remove(node.right, min_larger_node.id)

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

    def update(self, id):
        node = self.tree.find(self.tree.root, id)
        if node:
            quantity = int(input(f"Введіть нову кількість для товару: "))
            node.quantity = quantity
            print(f"Залишок товару з id {id} оновлено на {quantity}.")
        else:
            print(f"Товар з id {id} винесли цигани")

    def find_item(self, id):
        node = self.tree.find(self.tree.root, id)
        if node:
            return f"id: {id}, залишок: {node.quantity}"
        return None

    def print_inventory(self):
        print("Склад товарів:")
        if self.tree.root:
            self.tree.inorder(self.tree.root)
        else:
            print("Склад порожній")

    def clear_inventory(self):
        self.tree.root = None
        print("Склад очищено")

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            self._write_data(self.tree.root, f)

    def _write_data(self, node, file):
        if node:
            self._write_data(node.left, file)
            file.write(f"{node.id},{node.quantity}\n")
            self._write_data(node.right, file)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 2:
                        id_, quantity = int(parts[0]), int(parts[1])
                        self.insert(id_, quantity, silent=True)
        except FileNotFoundError:
            print("Файл не знайдено, створено новий склад")


def main():
    invent = Invent()
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_name = os.path.join(base_dir, "inventory_to_subtask", "inventory.txt")
    invent.load_from_file(file_name)

    while True:
        print(
            "\n1. Додати товар"
            "\n2. Оновити товар"
            "\n3. Видалити товар"
            "\n4. Пошук товару"
            "\n5. Показати складу"
            "\n6. Очистити склад"
            "\n7. Вийти зі складу"
        )

        command = input("\nВаш вибір: ")

        if command == "1":
            id_ = int(input("\nВведіть id: "))
            n = int(input("Введіть кількість: "))
            invent.insert(id_, n)

        elif command == "2":

            id_ = int(input("Введіть id: "))

            invent.update(id_)

        elif command == "3":
            id_ = int(input("Введіть id: "))
            invent.delete(id_)

        elif command == "4":
            id_ = int(input("Введіть id: "))
            result = invent.find_item(id_)
            print(result if result else "Товар не знайдено.")

        elif command == "5":
            invent.print_inventory()

        elif command == "6":
            invent.clear_inventory()

        elif command == "7":
            os.makedirs(os.path.dirname(file_name), exist_ok=True)
            invent.save_to_file(file_name)

            print("Ви покинули склад")
            break

        else:
            print("Не вірний вибір")


if __name__ == "__main__":
    main()
