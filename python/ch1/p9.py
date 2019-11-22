"""
 CREATED BY: Benjamin Hamlin
 Chapter 1 Question 9
 "String Rotation"
 PROMPT:
 Assume you have a method isSubstring which checks if one word is a substring of another.
 Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
 call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat")
 DATE: 11/18/2019
"""

import unittest

def isSubstring(str1, str2):
    if str2 in str1:
        return True
    return False

def p9(s1, s2):
    pass

class TestP9(unittest.TestCase):
    def test_p9(self):
        pass

if __name__ == '__main__':
    temp1 = input("Enter a string:")
    temp2 = input("Enter a string to see if it is a rotation of the other string:")
    print(p9(temp1, temp2))
