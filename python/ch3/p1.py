"""
 CREATED BY: Benjamin Hamlin
 Chapter 3 Question 1
 "Three in One"
 PROMPT:
 Describe how you could use a single array to implement three stacks

 IMPLEMENTATION:
 In the array every third element corresponds to one of the three stacks
 simple math to implement traversal of each stack
 DATE: 12/9/2019
"""

import unittest

class TripleStack:
    def __init__(self):
        self.stack = [None,None,None,None,None,None]
        self.top1 = 0
        self.top2 = 1
        self.top3 = 2

    def push(self, data, stack):
        if stack == 1:
            if self.top1 + 3 > len(self.stack):
                self.stack.append(None)
                self.stack.append(None)
                self.stack.append(None)
                self.stack.append(None)
                self.stack.append(None)
                self.stack.append(None)
            if not self.isEmpty(1):
                self.top1 += 3
            if self.stack[self.top1] is None:
                self.stack[self.top1] = data
            else:
                self.stack.insert(self.top1, data)
        elif stack == 2:
            if self.top2 + 3 > len(self.stack):
                self.stack.append(None)
                self.stack.append(None)
                self.stack.append(None)
                self.stack.append(None)
                self.stack.append(None)
                self.stack.append(None)
            if not self.isEmpty(2):
                self.top2 += 3
            if self.stack[self.top2] is None:
                self.stack[self.top2] = data
            else:
                self.stack.insert(self.top2, data)
        elif stack == 3:
            if self.top3 + 3 > len(self.stack):
                self.stack.append(None)
                self.stack.append(None)
                self.stack.append(None)
                self.stack.append(None)
                self.stack.append(None)
                self.stack.append(None)
            if not self.isEmpty(3):
                self.top3 += 3
            if self.stack[self.top3] is None:
                self.stack[self.top3] = data
            else:
                self.stack.insert(self.top3, data)

    def pop(self, stack):
        if stack == 1:
            temp = self.stack[self.top1]
            self.stack[self.top1] = None
            self.top1 -= 3
        elif stack == 2:
            temp = self.stack[self.top2]
            self.stack[self.top2] = None
            self.top2 -= 3
        elif stack == 3:
            temp = self.stack[self.top3]
            self.stack[self.top3] = None
            self.top3 -= 3
        return temp

    def isEmpty(self, stack):
        if stack == 1:
            if self.top1 == 0 and self.stack[self.top1] is None:
                return True
        elif stack == 2:
            if self.top2 == 1 and self.stack[self.top2] is None:
                return True
        elif stack == 3:
            if self.top3 == 2 and self.stack[self.top3] is None:
                return True
        return False

class TestP1(unittest.TestCase):
    def setUp(self):
        self.stack = TripleStack()

    def tearDown(self):
        self.stack = None

    def test_p1_push(self):
        self.stack.push(5,1)
        self.stack.push(7,1)
        self.stack.push(4,2)
        self.stack.push(4,3)
        self.stack.push(7,2)
        self.stack.push(5,3)
        # BUG: following causes bug described above insert()
        self.stack.push(6,3)
        self.assertFalse(self.stack.isEmpty(1))
        self.assertFalse(self.stack.isEmpty(2))
        self.assertFalse(self.stack.isEmpty(3))
        correct = [5,4,4,7,7,5,None,None,6,None,None,None]
        self.assertEqual(self.stack.stack, correct)

    def test_p1_push_bugfix(self):
        self.stack.push(5,1)
        self.stack.push(7,1)
        self.stack.push(5,2)
        self.assertEqual(self.stack.stack,[5,5,None,7,None,None])

    def test_p1_pop(self):
        self.stack.push(5,1)
        self.stack.push(7,1)
        self.stack.push(5,2)
        self.assertEqual(self.stack.stack,[5,5,None,7,None,None])
        self.assertEqual(self.stack.pop(1), 7)
        self.assertEqual(self.stack.stack,[5,5,None,None,None,None])
