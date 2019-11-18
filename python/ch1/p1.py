"""
 CREATED BY: Benjamin Hamlin
 Chapter 1 Question 1
 "Is Unique"
 PROMPT:
 Implement an algorithm to determine if a string has all unique characters.
 What if you cannot use additional data structures?
 DATE: 11/14/2019
"""

import unittest

# O(N) where N is the length of str
def p1(str):
    for letter in str:
        if str.count(letter) > 1:
            return False
    return True

class TestP1(unittest.TestCase):
    def test_p1(self):
        self.assertTrue(p1("abcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(p1("adapt"))
        self.assertTrue(p1("adept"))
        self.assertFalse(p1("digitation"))

if __name__ == '__main__':
    temp = input("Enter a string to see if all characters are unique:")
    print(p1(temp))
