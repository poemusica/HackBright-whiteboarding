class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right = node

    def get_value(self):
        return self.value

    def set_value(self, number):
        self.value = number

def depth_first_traversal(node):
    if node is None:
        return
    print node.value,

    depth_first_traversal(node.left)
    depth_first_traversal(node.right)

def breadth_first_traversal(node):
    

# TEST
# root = BinaryTreeNode(0)
# root.left = BinaryTreeNode(1)
# root.left.left = BinaryTreeNode(2)
# root.left.left.left = BinaryTreeNode(3)
# root.left.left.right = BinaryTreeNode(4)
# root.left.right = BinaryTreeNode(5)
# root.right = BinaryTreeNode(6)
# root.right.left = BinaryTreeNode(7)
# root.right.left.left = BinaryTreeNode(8)
# root.right.left.right = BinaryTreeNode(9)
# root.right.right = BinaryTreeNode(10)

# depth_first_traversal(root)
