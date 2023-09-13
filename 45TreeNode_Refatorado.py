# CÓDIGO REFATORADO

class BinaryTree2:
    class TreeNode2:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return self.TreeNode2(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.value)
            self._inorder_traversal(node.right)

    def find(self, value):
        return self._find(self.root, value)

    def _find(self, node, value):
        if not node:
            return None
        if node.value == value:
            return node
        if value < node.value:
            return self._find(node.left, value)
        return self._find(node.right, value)

tree = BinaryTree2()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.inorder_traversal()
found_node = tree.find(30)
if found_node:
    print(f"Found node with value: {found_node.value}")
else:
    print("Node not found.")
