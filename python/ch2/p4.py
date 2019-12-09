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

    def print(self):
        cur = self.head
        while cur.next is not None:
            print(cur.data)
            cur = cur.next
        print(cur.data)
        print()

# O(n)
def p4(list, partition):
    head = list.head
    while head.data < partition:
        head = head.next
    cur = head
    while cur is not None:
        if cur.data < partition:
            temp = head.data
            head.data = cur.data
            cur.data = temp
            head = head.next
        cur = cur.next
    return list

class TestP4(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def tearDown(self):
        self.list.dispose()
        self.list = None

    def test_p4_partOn5(self):
        correct = LinkedList()
        correct.head = Node(3)
        correct.head.next = Node(2)
        correct.head.next.next = Node(1)
        correct.head.next.next.next = Node(5)
        correct.head.next.next.next.next = Node(10)
        correct.head.next.next.next.next.next = Node(5)
        correct.head.next.next.next.next.next.next = Node(8)

        self.list.head = Node(3)
        self.list.head.next = Node(5)
        self.list.head.next.next = Node(8)
        self.list.head.next.next.next = Node(5)
        self.list.head.next.next.next.next = Node(10)
        self.list.head.next.next.next.next.next = Node(2)
        self.list.head.next.next.next.next.next.next = Node(1)

        # self.list.print()
        self.list = p4(self.list, 5)
        # self.list.print()

        cur1 = self.list.head
        cur2 = correct.head
        while(cur1 != None and cur2 != None):
            self.assertEqual(cur1.data,cur2.data)
            cur1 = cur1.next
            cur2 = cur2.next
        correct.dispose()

    def test_p4_partOn7(self):
        correct = LinkedList()
        correct.head = Node(3)
        correct.head.next = Node(5)
        correct.head.next.next = Node(5)
        correct.head.next.next.next = Node(2)
        correct.head.next.next.next.next = Node(1)
        correct.head.next.next.next.next.next = Node(8)
        correct.head.next.next.next.next.next.next = Node(10)

        self.list.head = Node(3)
        self.list.head.next = Node(5)
        self.list.head.next.next = Node(8)
        self.list.head.next.next.next = Node(5)
        self.list.head.next.next.next.next = Node(10)
        self.list.head.next.next.next.next.next = Node(2)
        self.list.head.next.next.next.next.next.next = Node(1)

        self.list = p4(self.list, 7)
        # self.list.print()

        cur1 = self.list.head
        cur2 = correct.head
        while(cur1 != None and cur2 != None):
            self.assertEqual(cur1.data,cur2.data)
            cur1 = cur1.next
            cur2 = cur2.next
        correct.dispose()
