"""
 CREATED BY: Benjamin Hamlin
 Chapter 2 Question 3
 "Delete Middle Node"
 PROMPT:
 Implement an algorithm to delete a node in the middle(i.e, any node but the first and last node, not necessarily the exact middle)
 of a singly linked list, given only access to that node.
 DATE: 12/6/2019
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

def p3(node):
    cur = node
    while cur.next is not None:
        cur.data = cur.next.data
        cur.next = cur.next.next
    cur.next = None

class TestP3(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def tearDown(self):
        self.list.dispose()
        self.list = None

    def test_p3_4_elements(self):
        correct = LinkedList()
        correct.head = Node(1)
        correct.head.next = Node(2)
        correct.head.next.next = Node(4)

        self.list.head = Node(1)
        second = Node(2)
        third = Node(3)
        fourth = Node(4)
        self.list.head.next = second
        second.next = third
        third.next = fourth

        p3(third)

        cur1 = self.list.head
        cur2 = correct.head
        while(cur1 != None and cur2 != None):
            self.assertEqual(cur1.data,cur2.data)
            cur1 = cur1.next
            cur2 = cur2.next
        if (cur1 is None and cur2 is not None) or (cur1 is not None and cur2 is None):
            self.assertTrue(False)
