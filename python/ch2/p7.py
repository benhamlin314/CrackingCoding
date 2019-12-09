"""
 CREATED BY: Benjamin Hamlin
 Chapter 2 Question 7
 "Intersection"
 PROMPT:
 Given two singly linked lists, determine if the two lists intersect.
 Return the intersecting node. Note that the intersection is defined based on
 reference, not value. That is, if the kth node of the first list and the
 jth node of the second are the same node by reference, then they are
 intersecting
 DATE: 12/9/2019
"""

import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def dispose(self):
        del self

class LinkedList:
    def __init__(self):
        self.head = None

    def dispose(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp.dispose()
            self.dispose()

# O(M*N) where m is the length of list1 and n is the length of list2
def p7(list1, list2):
    cur1 = list1.head
    cur2 = list2.head
    while cur1 is not None:
        while cur2 is not None:
            if cur1 is cur2:
                return cur1
            cur2 = cur2.next
        cur1 = cur1.next
        cur2 = list2.head
    return None

class TestP7(unittest.TestCase):
    def setUp(self):
        self.list1 = LinkedList()
        self.list2 = LinkedList()

    def tearDown(self):
        self.list1.dispose()
        self.list2.dispose()
        self.list1 = None
        self.list2 = None

    def test_p7(self):
        self.list1.head = Node(1)
        second = Node(2)
        third = Node(3)
        fourth = Node(4)
        fifth = Node(5)
        sixth = Node(6)
        self.list1.head.next = second
        second.next = third
        third.next = fourth
        fourth.next = fifth
        fifth.next = sixth

        self.list2.head = Node(2)
        self.list2.head.next = fourth

        self.assertEqual(p7(self.list1, self.list2), fourth)

    def test_p7_none(self):
        self.list1.head = Node(1)
        self.list1.head.next = Node(2)
        self.list1.head.next.next = Node(3)
        self.list2.head = Node(4)
        self.list2.head.next = Node(5)
        self.list2.head.next.next = Node(6)

        self.assertEqual(p7(self.list1, self.list2), None)
