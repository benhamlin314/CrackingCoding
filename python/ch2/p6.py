"""
 CREATED BY: Benjamin Hamlin
 Chapter 2 Question 6
 "Palindrome"
 PROMPT:
 Implement a function to check if a linked list is a palindrome

 NOTE:
 I assume doubly linked list to make navigating list easier and
 cut down on time complexity
 DATE: 12/9/2019
"""

import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def dispose(self):
        del self

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_tail(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp

    def length(self):
        count = 0
        cur = self.head
        while cur is not self.tail:
            count += 1
            cur = cur.next
        return count

    def dispose(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp.dispose()
            self.dispose()

def p6(list):
    count = 0
    len = list.length()
    begin = list.head
    end = list.tail
    while begin is not end and count < len/2:
        if begin.data != end.data:
            return False
        else:
            begin = begin.next
            end = end.prev
    return True

class TestP6(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def tearDown(self):
        self.list.dispose()
        self.list = None

    def test_p6_racecar(self):
        self.list.add_tail('r')
        self.list.add_tail('a')
        self.list.add_tail('c')
        self.list.add_tail('e')
        self.list.add_tail('c')
        self.list.add_tail('a')
        self.list.add_tail('r')
        self.assertTrue(p6(self.list))

    def test_p6_food(self):
        self.list.add_tail('f')
        self.list.add_tail('o')
        self.list.add_tail('o')
        self.list.add_tail('d')
        self.assertFalse(p6(self.list))

    def test_p6_cammac(self):
        self.list.add_tail('c')
        self.list.add_tail('a')
        self.list.add_tail('m')
        self.list.add_tail('m')
        self.list.add_tail('a')
        self.list.add_tail('c')
        self.assertTrue(p6(self.list))
