"""
 CREATED BY: Benjamin Hamlin
 Chapter 3 Question 5
 "Sort Stack"
 PROMPT:
 Write a program to sort a stack such that the smallest items are on the top.
 You can use an addition temporary stack, but you may not copy the elements into
 any other data structure such as an array. The stack supports the following
 operations: push, pop, peek, and isEmpty
 DATE: 12/10/2019
"""

import unittest
from ch3.p2 import MinStack

class SortStack:
    def __init__(self):
        self.stack = MinStack()

    def push(self, data):
        if not self.isEmpty():
            temp = MinStack()
            while not self.isEmpty() and self.peek() < data:
                temp.push(self.stack.pop())
            self.stack.push(data)
            while not temp.isEmpty():
                self.stack.push(temp.pop())
        else:
            self.stack.push(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        temp = self.stack.pop()
        if temp is not None:
            self.stack.push(temp)
        else:
            temp = 0
        return temp

    def isEmpty(self):
        return self.stack.isEmpty()

class TestP5(unittest.TestCase):
    def setUp(self):
        self.stack = SortStack()

    def tearDown(self):
        self.stack = None

    def test_p5_push(self):
        for x in range(0,20):
            self.stack.push(x)
        self.assertEqual(self.stack.stack.stack, [19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0])

    def test_p5_pop(self):
        for x in range(0,20):
            self.stack.push(x)
        self.assertEqual(self.stack.stack.stack, [19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0])
        self.assertEqual(self.stack.pop(),0)
        self.assertEqual(self.stack.pop(),1)
        self.assertEqual(self.stack.stack.stack, [19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2])

    def test_p5_peek(self):
        for x in range(0,20):
            self.stack.push(x)
        self.assertEqual(self.stack.stack.stack, [19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0])
        self.assertEqual(self.stack.peek(), 0)
        self.assertEqual(self.stack.stack.stack, [19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0])

    def test_p5_isEmpty(self):
        self.assertTrue(self.stack.isEmpty())
        self.stack.push(0)
        self.assertFalse(self.stack.isEmpty())
