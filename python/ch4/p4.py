"""
 CREATED BY: Benjamin Hamlin
 Chapter 4 Question 4
 "Check Balanced"
 PROMPT:
 Implement a function to check if a binary tree is balanced. For the purpose of
 this question, a balanced tree is defined to be a tree such that the heights of
 the two subtrees of any node never differ by more than one
 DATE: 12/11/2019
"""

import unittest
from ch4.btree import BTNode, BinaryTree

def __p4(node: BTNode):
    if node is None:
        return 0
    return max(__p4(node.left), __p4(node.right)) + 1

def p4(node: BTNode):
    if node is None:
        return True

    left = __p4(node.left)
    right = __p4(node.right)

    if (abs(left - right) <= 1) and p4(node.left) and p4(node.right):
        return True

    return False

class TestP4(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def tearDown(self):
        self.tree = None

    def test_p4_false(self):
        self.tree.root = BTNode(1)
        self.tree.root.left = BTNode(2)
        self.tree.root.right = BTNode(3)
        self.tree.root.left.left = BTNode(4)
        self.tree.root.left.right = BTNode(5)
        self.tree.root.left.left.left = BTNode(8)
        self.assertFalse(p4(self.tree.root))

    def test_p4_true(self):
        self.tree.root = BTNode(1)
        self.tree.root.left = BTNode(2)
        self.tree.root.right = BTNode(3)
        self.tree.root.left.left = BTNode(4)
        self.tree.root.left.right = BTNode(5)
        self.assertTrue(p4(self.tree.root))
