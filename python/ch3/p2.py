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
        self.min = 0

    def push(self, data):
        self.stack.append(data)
        if not self.stack.isEmpty():
            self.top += 1
            if self.stack[self.min] > data:
                self.min = self.top

    def pop(self):
        if not self.stack.isEmpty():
            temp = self.stack.pop()
            self.top -= 1
            return temp

    def isEmpty(self):
        if self.stack.count() == 0:
            return True
        return False

    def min(self):
        return self.stack[self.min]

class TestP2(unittest.TestCase):
    def setUp(self):
        self.stack = MinStack()

    def tearDown(self):
        self.stack = None

    def test_p2_push(self):
        pass

    def test_p2_pop(self):
        pass

    def test_p2_min(self):
        pass
