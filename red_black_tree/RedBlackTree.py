class RedBlackTree:
    def __init__(self):
        self.root = None
        self.nil = Node()

    def _left_rotate(self, x):
        pass

    def _right_rotate(self, x):
        pass

    def insert(self, key):
        pass

    def delete(self, key):
        pass

class Node:
    BLACK, RED = range(2)

    def __init__(self, key=None, color=BLACK, left=None, right=None, p=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.p = p
