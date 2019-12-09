"""
 CREATED BY: Benjamin Hamlin
 Chapter 2 Question 5
 "Sum Lists"
 PROMPT:
 You have two numbers represented by a linked list, where each node contains
  a single digit. The digits are stored in reverse order, such that the 1's
 digit is at the head of the list. Write a function that adds the two numbers
 and returns the sum as a linked list. (You are not allowed to "cheat" and just
 convert the linked list to an integer.)

 FOLLOW UP
 Solve the above problem with the digits stored in forward order.
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

# O(n) where n is the greatest length of the two inputs
def p5_reverse(n1, n2):
    ans = LinkedList()
    carry = 0
    cur1 = n1.head
    cur2 = n2.head
    temp = cur1.data + cur2.data
    if temp >= 10:
        carry = temp/10
        temp = temp%10
    ans.head = Node(temp)
    curAns = ans.head
    cur1 = cur1.next
    cur2 = cur2.next
    while cur1 is not None and cur2 is not None:
        temp = cur1.data + cur2.data + carry
        carry = 0
        if temp >= 10:
            carry = int(temp/10)
            temp = int(temp%10)
        curAns.next = Node(temp)
        curAns = curAns.next
        cur1 = cur1.next
        cur2 = cur2.next
    if cur1 is not None:
        while cur1 is not None:
            temp = cur1.data + carry
            carry = 0
            curAns.next = Node(temp)
    if cur2 is not None:
        while cur2 is not None:
            temp = cur2.data + carry
            carry = 0
            curAns.next = Node(temp)
    return ans

def p5_forward(n1, n2):
    ans = LinkedList()
    carry = 0
    cur1 = n1.head
    cur2 = n2.head
    temp = cur1.data + cur2.data
    if temp >= 10:
        carry = temp/10
        temp = temp%10
    if carry != 0:
        ans.head = Node(carry)
    if ans.head is None:
        ans.head = Node(temp)
        curAns = ans.head
    else:
        ans.head.next = Node(temp)
        curAns = ans.head.next
    pass

class TestP5(unittest.TestCase):
    def setUp(self):
        self.list1 = LinkedList()
        self.list2 = LinkedList()

    def tearDown(self):
        self.list1.dispose()
        self.list2.dispose()
        self.list1 = None
        self.list2 = None

    def test_p5_reverse(self):
        correct = LinkedList()
        correct.head = Node(2)
        correct.head.next = Node(1)
        correct.head.next.next = Node(9)

        self.list1.head = Node(7)
        self.list1.head.next = Node(1)
        self.list1.head.next.next = Node(6)

        self.list2.head = Node(5)
        self.list2.head.next = Node(9)
        self.list2.head.next.next = Node(2)

        answer = p5_reverse(self.list1, self.list2)

        cur1 = answer.head
        cur2 = correct.head
        while(cur1 != None and cur2 != None):
            self.assertEqual(cur1.data,cur2.data)
            cur1 = cur1.next
            cur2 = cur2.next
        correct.dispose()
