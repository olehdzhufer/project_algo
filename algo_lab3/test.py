import unittest
from main import invert_binary_tree, BinaryTree

class TestBinaryTreeInversion(unittest.TestCase):
    def test_invert_binary_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)

        inverted_root = invert_binary_tree(root)

        self.assertEqual(inverted_root.value, 1)
        self.assertEqual(inverted_root.left.value, 3)
        self.assertEqual(inverted_root.right.value, 2)
        self.assertEqual(inverted_root.right.left.value, 5)
        self.assertEqual(inverted_root.right.right.value, 4)



if __name__ == '__main__':
    unittest.main()