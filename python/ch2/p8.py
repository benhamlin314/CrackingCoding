"""
 CREATED BY: Benjamin Hamlin
 Chapter 2 Question 8
 "Loop Detection"
 PROMPT:
 Given a linked list which might contain a loop, implement and algorithm that
 returns the node at the beginning of the loop (if one exists)
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
            # self.dispose()

# at this time I am unable to determine the time complexity without more studying
def p8(list):
    """cur1 = list.head.next
    cur2 = list.head.next
    head = list.head
    while head is not cur1 and head is not cur2:
        while cur1 is not cur2:
            cur1 = cur1.next
            cur2 = cur2.next.next
        head = head.next
        cur1 = head.next
        cur2 = head.next
        #print(head.data)
        #print(cur1.data)
        #print(cur2.data)
    if head is cur1 or head is cur2:
        return head
    else:
        return None
    NOTE: INCORRECT
    Research found floyd's tortoise and hare algorithm
    implemented below
    """
    t = list.head.next
    h = list.head.next.next
    while t is not h:
        t = t.next
        h = h.next.next

    mu = 0
    t = list.head
    while t is not h:
        t = t.next
        h = h.next
        mu += 1
    return t

    """
    # rest of floyd's algorithm unnecessary
    lam = 1
    h = t.next
    while t is not h:
        h = h.next
        lam += 1
    """

class TestP8(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def tearDown(self):
        self.list.dispose()
        self.list = None

    def test_p8(self):
        self.list.head = Node('A')
        self.list.head.next = Node('B')
        C = Node('C')
        self.list.head.next.next = C
        C.next = Node('D')
        C.next.next = Node('E')
        C.next.next.next = C

        self.assertEqual(p8(self.list).data, C.data)
