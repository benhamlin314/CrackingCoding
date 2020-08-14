"""
 CREATED BY: Benjamin Hamlin
 Chapter 4 Question 9
 "BST Sequence"
 PROMPT:
 A binary search tree was created by traversing through an array from left to
 right and inserting each element. Given a binary search tree with distinct
 elements, print all possible arrays that could have led to this tree.
 DATE: 12/15/2019
"""

import unittest
from ch4.btree import BTNode, BinaryTree

def p9(tree: BinaryTree):
    ans = []
    arr = []


class TestP9(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def tearDown(self):
        self.tree = None

    def test_p9(self):
        pass
