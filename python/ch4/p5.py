"""
 CREATED BY: Benjamin Hamlin
 Chapter 4 Question 5
 "Validate BST"
 PROMPT:
 Implement a function to check if a binary tree is a BST
 DATE: 12/12/2019
"""

import unittest
from ch4.btree import BTNode, BinaryTree

def __p5(node: BTNode):
    if node.left is not None:
        if node.left.data < node.data:
            __p5(node.left)
        else:
            return False
    if node.right is not None:
        if node.right.data > node.data:
            __p5(node.right)
        else:
            return False

def p5(tree: BinaryTree):
    if tree.root is None:
        return True
    if tree.root.left is None and tree.root.right is None:
        return True
    rest = __p5(tree.root)
    if rest is not None:
        return False
    else:
        return True

class TestP5(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def tearDown(self):
        self.tree = None

    def test_p5_bst(self):
        self.tree.root = BTNode(5)
        self.tree.root.left = BTNode(2)
        self.tree.root.left.left = BTNode(1)
        self.tree.root.left.right = BTNode(3)
        self.tree.root.right = BTNode(7)
        self.tree.root.right.left = BTNode(6)
        self.tree.root.right.right = BTNode(8)
        self.assertTrue(p5(self.tree))

    def test_p5_notBst(self):
        self.tree.root = BTNode(5)
        self.tree.root.left = BTNode(10)
        self.tree.root.left.left = BTNode(1)
        self.tree.root.left.right = BTNode(3)
        self.tree.root.right = BTNode(7)
        self.tree.root.right.left = BTNode(6)
        self.tree.root.right.right = BTNode(8)
        self.assertFalse(p5(self.tree))
