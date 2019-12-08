"""
 CREATED BY: Benjamin Hamlin
 Chapter 2 Question 2
 "Return Kth to Last"
 PROMPT:
 Implement an algorithm to find the kth to last element of a singly linked list
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

    def length(self):
        cur = self.head
        count = 0
        while cur.next is not None:
            cur = cur.next
            count = count + 1
        return count

# O(n)
def p2(list, k):
    tot = list.length()
    ans = tot - k
    cur = list.head
    while ans > 0:
        cur = cur.next
        ans = ans - 1
    return cur

class TestP2(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def tearDown(self):
        self.list.dispose()
        self.list = None

    def test_p2_2nd(self):
        self.list.head = Node(1)
        second = Node(2)
        third = Node(3)
        fourth = Node(4)
        self.list.head.next = second
        second.next = third
        third.next = fourth

        self.assertEqual(p2(self.list,2).data, 2)
