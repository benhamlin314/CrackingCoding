"""
 CREATED BY: Benjamin Hamlin
 Chapter 3 Question 4
 "Queue via Stacks"
 PROMPT:
 Implement a MyQueue class which implements a queue using two stacks

 Note:
 Utilizing MinStack rather than writing another stack class for simplicity
 DATE: 12/10/2019
"""

import unittest
from ch3.p2 import MinStack

class MyQueue:
    def __init__(self):
        self.primaryStack = MinStack()
        self.secondaryStack = MinStack()

    def add(self, data):
        while not self.isEmpty():
            self.secondaryStack.push(self.primaryStack.pop())
        self.primaryStack.push(data)
        while not self.secondaryStack.isEmpty():
            self.primaryStack.push(self.secondaryStack.pop())

    def remove(self):
        return self.primaryStack.pop()

    def peek(self):
        temp = self.primaryStack.pop()
        self.primaryStack.push(temp)
        return temp

    def isEmpty(self):
        return self.primaryStack.isEmpty()

class TestP4(unittest.TestCase):
    def setUp(self):
        self.q = MyQueue()

    def tearDown(self):
        self.q = None

    def test_p4_add(self):
        for x in range(0,20):
            self.q.add(x)
        self.assertEqual(self.q.peek(), 0)

    def test_p4_remove(self):
        self.q.add(2)
        self.q.add(3)
        self.q.add(4)
        self.assertEqual(self.q.remove(), 2)

    def test_p4_peek(self):
        self.q.add(2)
        self.q.add(3)
        self.q.add(4)
        self.assertEqual(self.q.peek(),2)

    def test_p4_isEmpty(self):
        self.assertTrue(self.q.isEmpty())
        self.q.add(1)
        self.assertFalse(self.q.isEmpty())
