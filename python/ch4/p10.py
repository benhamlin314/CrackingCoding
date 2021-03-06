"""
 CREATED BY: Benjamin Hamlin
 Chapter 4 Question 10
 "Check Subtree"
 PROMPT:
 T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create
 an algorithm to determine if T2 is a subtree of T1.
 A tree T2 is a subtree of T1 if there exists a node n in T1 such that the
 subtree of n is identical to T2. That is, if you cut off the tree at node n,
 the two trees would be identical.
 DATE: 12/15/2019
"""

import unittest
from ch4.btree import BTNode, BinaryTree

def p10(T1: BinaryTree,T2: BinaryTree):
    pass

class TestP10(unittest.TestCase):
    def setUp(self):
        self.t1 = BinaryTree()
        self.t2 = BinaryTree()

    def tearDown(self):
        self.t1 = None
        self.t2 = None

    def test_p10(self):
        pass
