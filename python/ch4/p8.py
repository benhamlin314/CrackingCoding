"""
 CREATED BY: Benjamin Hamlin
 Chapter 4 Question 8
 "First Common Ancestor"
 PROMPT:
 Design an algorithm and write code to find the first common ancestor of two
 nodes in a binary tree. Avoid storing additional nodes in a data structure.
 NOTE: This is not necessarily a binary search tree.

 Implement:
 Assumed parent pointer exists

 FOLLOW UP:
 without parent pointer
 DATE: 12/15/2019
"""

import unittest
from ch4.btree import BTNode.root, BinaryTree

class BTPNode(BTNode):
    def __init__(self, data):
        super().__init__(data)
        self.parent = None

# O(N*M) where n is the depth of n1 and m is the depth of n2
def p8_parent(tree: BinaryTree, n1: BTPNode, n2: BTPNode):
    root = tree.root
    cur1 = n1.parent
    while cur1 is not root:
        cur2 = n2.parent
        while cur2 is not root:
            if cur2 is cur1:
                return cur2
            cur2 = cur2.parent
        cur1 = cur1.parent
    return root

def p8_noparent(tree: BinaryTree, n1: BTNode, n2: BTNode):
    pass

class TestP8(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def tearDown(self):
        self.tree = None

    def test_p8_parent(self):
        self.tree.root = BTPNode(5)
        left = BTPNode(8)
        right = BTPNode(40)
        self.tree.root.left = left
        self.tree.root.right = right
        left.parent = self.tree.root
        right.parent = self.tree.root
        ll = BTPNode(60)
        left.left = ll
        rr = BTPNode(33)
        lr = BTPNode(23)
        rl = BTPNode(32)
        left.right = lr
        right.right = rr
        right.left = rl
        ll.parent = left
        lr.parent = left
        rl.parent = right
        rr.parent = right
        lll = BTPNode(80)
        lrr = BTPNode(49)
        lll.parent = ll
        lrr.parent = lr
        self.assertEqual(p8_parent(self.tree, lll, lrr), left)

    @unittest.skip("NoParent not implemented")
    def test_p8_noparent(self):
        pass
