"""
 CREATED BY: Benjamin Hamlin
 Chapter 4 Question 3
 "List of Depths"
 PROMPT:
 Given a binary tree, design an algorithm which creates a linked list of all the
 nodes at each depth (e.g., if you have a tree with depth D, you'll have D Linked
 Lists)
 DATE: 12/11/2019
"""

import unittest
from ch4.btree import BTNode,  BinaryTree
from ch4.linkedlist import LLNode, LinkedList

def __p3(arr, node: BTNode, level):
    if node.left is not None:
        __p3(arr, node.left, level+1)
    try:
        arr[level].add(node)
    except IndexError:
        arr.append(LinkedList())
    if node.right is not None:
        __p3(arr, node.right, level+1)

def p3(tree: BinaryTree):
    arr = []
    __p3(arr, tree.root, 0)
    return arr

class TestP3(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def tearDown(self):
        self.tree = None

    def test_p3(self):
        self.tree.add(BTNode(5))
        for x in range(10):
            self.tree.add(BTNode(x))
        self.assertEqual(len(p3(self.tree)), 6)

    def test_p3_D2(self):
        self.tree.add(BTNode(5))
        self.tree.add(BTNode(2))
        self.tree.add(BTNode(7))
        self.assertEqual(len(p3(self.tree)), 2)
