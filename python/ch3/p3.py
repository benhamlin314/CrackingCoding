"""
 CREATED BY: Benjamin Hamlin
 Chapter 3 Question 3
 "Stack of Plates"
 PROMPT:
 Imagine a literal stack of plates. If the stack gets too high, it might topple.
 Therefore, in real life, we would likely start a new stack when the previous
 stack exceeds a threshold
 DATE: 12/10/2019
"""

import unittest

class SetOfStacks:
    def __init__(self, threshold):
        self.stack = [[]]
        self.thresh = threshold
        self.subStackIndex = 0

    def push(self,data):
        """
        pushes data to the top of the stack closest to the start of the set of stacks
        """
        try:
            cur = 0
            while self.isFull(cur):
                cur += 1
            self.stack[cur].append(data)
        except IndexError:
            self.stack.append([])
            self.subStackIndex += 1
            self.stack[self.subStackIndex].append(data)


    def pop(self):
        if len(self.stack[self.subStackIndex]) == 1:
            temp = self.stack[self.subStackIndex].pop()
            self.stack.pop(self.subStackIndex)
            self.subStackIndex -= 1
            return temp
        return self.stack[self.subStackIndex].pop()

    def popAt(self,subStack):
        if len(self.stack[subStack]) == 1:
            temp = self.stack[subStack].pop()
            self.stack.pop(subStack)
            subStackIndex -= 1
            return temp
        return self.stack[subStack].pop()

    def isFull(self, subStack=None):
        if subStack is not None:
            if len(self.stack[subStack]) == self.thresh:
                return True
            return False
        else:
            return self.isFull(self.subStackIndex)

class TestP3(unittest.TestCase):
    def setUp(self):
        self.stack = SetOfStacks(4)

    def tearDown(self):
        self.stack = None

    def test_p3_push(self):
        for x in range(0,20):
            self.stack.push(x)
        self.assertEqual(self.stack.stack, [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[16,17,18,19]])
        self.stack.popAt(3)
        self.assertEqual(self.stack.stack, [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14],[16,17,18,19]])
        self.stack.push(15)
        self.assertEqual(self.stack.stack, [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[16,17,18,19]])

    def test_p3_pop(self):
        for x in range(0,20):
            self.stack.push(x)
        self.assertEqual(self.stack.stack, [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[16,17,18,19]])
        self.assertEqual(self.stack.pop(),19)
        self.assertEqual(self.stack.stack, [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[16,17,18]])

    def test_p3_popAt(self):
        for x in range(0,20):
            self.stack.push(x)
        self.assertEqual(self.stack.stack, [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[16,17,18,19]])
        self.stack.popAt(3)
        self.assertEqual(self.stack.stack, [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14],[16,17,18,19]])

    def test_p3_isFull(self):
        self.assertFalse(self.stack.isFull())
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.assertTrue(self.stack.isFull())
        self.stack.push(5)
        self.assertFalse(self.stack.isFull())
        self.assertEqual(self.stack.stack,[[1,2,3,4],[5]])
