"""
 CREATED BY: Benjamin Hamlin
 Chapter 2 Question 4
 "Partition"
 PROMPT:
 Write code to partition a linked list around a value x, such that all nodes
 less than x come before all nodes greater than or equal to x. (IMPORTANT: the
 partition element x can appear anywhere in the "right parition"; it does not
  need to appear between the left and right partitions)
 DATE: 12/8/2019
"""

import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def dispose(self):
        del self

def p4(list, partition):
    pass

class TestP4(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def tearDown(self):
        self.list.dispose()
        self.list = None

    def test_p4(self):
        pass
