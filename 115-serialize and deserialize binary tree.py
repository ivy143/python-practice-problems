#serialize and deserialize binary tree problem
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        def helper(node):
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            helper(node.left)
            helper(node.right)

        vals = []
        helper(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def helper():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node

        vals = iter(data.split())
        return helper()
# Example usage
codec = Codec()
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
serialized = codec.serialize(root)
print("Serialized tree:", serialized)
deserialized_root = codec.deserialize(serialized)
print("Deserialized tree root value:", deserialized_root.val)  # Output: Deserialized tree root value: 1