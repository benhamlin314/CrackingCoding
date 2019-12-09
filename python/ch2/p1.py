"""
 CREATED BY: Benjamin Hamlin
 Chapter 2 Question 1
 "Remove Dups"
 PROMPT:
 Write code to remove duplicates form an unsorted linked list.
 FOLLOW UP
 How would you solve this problem if a temporary buffer is not allowed?
 DATE: 12/4/2019
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

def p1(list):
    temp = list.head.data
    cur = list.head
    this = cur.next
    while(cur.next != None):
        while (this.next != None):
            if this.next.data == temp:
                rem = this.next
                this.next = rem.next
                del rem
            this = this.next
        cur = cur.next
        temp = cur.data
        this = cur.next
    return list.head

class TestP1(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def tearDown(self):
        self.list.dispose()
        self.list = None

    def test_p1_dup1(self):
        correct = LinkedList()
        correct.head = Node(1)
        correct.head.next = Node(2)
        correct.head.next.next = Node(3)
        correct.head.next.next.next = Node(4)

        self.list.head = Node(1)
        second = Node(2)
        third = Node(3)
        fourth = Node(1)
        fifth = Node(4)
        self.list.head.next = second
        second.next = third
        third.next = fourth
        fourth.next = fifth

        cur1 = p1(self.list)
        cur2 = correct.head
        while(cur1 != None and cur2 != None):
            self.assertEqual(cur1.data,cur2.data)
            cur1 = cur1.next
            cur2 = cur2.next
