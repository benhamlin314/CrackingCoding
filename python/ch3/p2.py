"""
 CREATED BY: Benjamin Hamlin
 Chapter 3 Question 2
 "Stack Min"
 PROMPT:
 How would you design a stack in which, in addition to push and pop, has a function
 min in which returns the minimum element? Push, pop, and min should be O(1)
 DATE: 12/9/2019
"""

import unittest

class MinStack:
    def __init__(self):
        self.stack = []
        self.top = 0
        self.minIndex = 0

    def push(self, data):
        if not self.isEmpty():
            self.stack.append(data)
            self.top += 1
            if self.stack[self.minIndex] > data:
                self.minIndex = self.top
        else:
            self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            temp = self.stack.pop()
            self.top -= 1
            return temp

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False

    def min(self):
        return self.stack[self.minIndex]

class TestP2(unittest.TestCase):
    def setUp(self):
        self.stack = MinStack()

    def tearDown(self):
        self.stack = None

    def test_p2_isEmpty(self):
        self.assertTrue(self.stack.isEmpty())
        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty())

    def test_p2_push(self):
        self.assertTrue(self.stack.isEmpty())
        self.stack.push(10)
        self.stack.push(15)
        self.stack.push(11)
        self.stack.push(5)
        self.assertEqual(self.stack.stack,[10,15,11,5])
        self.assertEqual(self.stack.min(),5)

    def test_p2_pop(self):
        self.stack.push(5)
        self.stack.push(10)
        self.stack.push(1)
        self.assertEqual(self.stack.stack,[5,10,1])
        self.assertEqual(self.stack.pop(),1)
        self.assertEqual(self.stack.stack,[5,10])

    def test_p2_min(self):
        self.stack.push(20)
        self.stack.push(10)
        self.assertEqual(self.stack.min(),10)
        self.stack.push(5)
        self.assertEqual(self.stack.min(),5)
        self.stack.push(50)
        self.assertEqual(self.stack.min(),5)
