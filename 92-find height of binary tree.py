#find height of binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(current_node.right, data)

    def height(self, node):
        if node is None:
            return -1  # Height of empty tree is -1
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1
# Example usage
bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)

print("Height of the binary tree:", bt.height(bt.root))  # Output: 2
