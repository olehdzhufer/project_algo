class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def invert_binary_tree(root: BinaryTree):
    if root is None:
        return None
    temp = root.right
    root.right = root.left
    root.left = temp

    if root.left:
        invert_binary_tree(root.left)
    if root.right:
        invert_binary_tree(root.right)

    return root

def print_1(root):
    if root is not None:
        print(root.value)
        print_1(root.left)
        print_1(root.right)

root = BinaryTree(10)
root.left = BinaryTree(5)
root.right = BinaryTree(18)
root.right.left = BinaryTree(12)
root.right.right = BinaryTree(22)
result = invert_binary_tree(root)
print_1(result)


