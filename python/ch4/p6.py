"""
 CREATED BY: Benjamin Hamlin
 Chapter 4 Question 6
 "Successor"
 PROMPT:
 Write an algorithm to find the "next" node (i.e., in-order successor) of a
 given node in a binary search tree. You may assume that each node has a link to
 its parents
 DATE: 12/12/2019
"""

import unittest
from ch4.btree import BTNode, BinaryTree

class BSTNode(BTNode):
    def __init__(self, data, parent):
        super().__init__(data)
        self.parent = parent

def p6(node: BSTNode):
    cur = None
    if node.right is not None:
        cur = node.right
        while cur.left is not None:
            cur = cur.left
        return cur
    else:
        cur = node
        parent = cur.parent
        while parent is not None and parent.left is not cur:
            cur = parent
            parent = cur.parent
        return parent

class TestP6(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def tearDown(self):
        self.tree = None

    def test_p6(self):
        self.tree.root = BSTNode(5, None)
        self.tree.root.left = BSTNode(2, self.tree.root)
        self.tree.root.left.left = BSTNode(1, self.tree.root.left)
        self.tree.root.left.right = BSTNode(3, self.tree.root.left)
        right = BSTNode(7, self.tree.root)
        self.tree.root.right = right
        lr = BSTNode(6, right)
        self.tree.root.right.left = lr
        self.tree.root.right.right = BSTNode(8, right)

        self.assertEqual(p6(self.tree.root), lr)

    def test_p6_parent(self):
        self.tree.root = BSTNode(5, None)
        self.tree.root.left = BSTNode(2, self.tree.root)
        self.tree.root.left.left = BSTNode(1, self.tree.root.left)
        self.tree.root.left.right = BSTNode(3, self.tree.root.left)
        right = BSTNode(7, self.tree.root)
        self.tree.root.right = right
        self.tree.root.right.right = BSTNode(8, right)
        self.assertEqual(p6(self.tree.root), right)
