#CÓDIGO ORIGINAL ANTES DA REFATORAÇÃO

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(node, value):
    if not node:
        return TreeNode(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value)
        inorder_traversal(node.right)

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
inorder_traversal(root)

