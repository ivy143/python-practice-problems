#level order traversal of tree
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

    def level_order_traversal(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            print(current_node.data, end=" ")
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
# Example usage
bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)

print("Level order traversal of the binary tree:")
bt.level_order_traversal()  # Output: 10 5 15 3 7 