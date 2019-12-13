"""
 CREATED BY: Benjamin Hamlin
 Chapter 4 Question 2
 "Minimal Tree"
 PROMPT:
 Given a sorted ascending array with unique integer elements, write an algorithm
 to create a binary search tree with minimal height
 DATE: 12/11/2019
"""

import unittest
from ch4.btree import BTNode, BinaryTree
import sys

sys.setrecursionlimit(10**6)

def p2(arr, tree):
    if len(arr) > 2:
        mid = len(arr)/2
        mid = int(mid)
        left = arr[:mid]
        tree.add(BTNode(arr.pop(mid)))
        right = arr[mid:]
        p2(left, tree)
        p2(right, tree)
    else:
        if len(arr) == 2:
            tree.add(BTNode(arr.pop()))
            tree.add(BTNode(arr.pop()))
        elif len(arr) == 1:
            tree.add(BTNode(arr.pop()))

class TestP2(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def tearDown(self):
        self.tree = None

    def test_p2(self):
        arr = []
        for x in range(0,21):
            arr.append(x)
        p2(arr, self.tree)
        arr.clear()
        for x in range(0,21):
            arr.append(x)
        self.assertEqual(self.tree.arrify(), arr)
