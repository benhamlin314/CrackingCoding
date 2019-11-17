"""
 CREATED BY: Benjamin Hamlin
 Chapter 1 Question 3
 "URLify"
 PROMPT:
 Write a method to replace all spaces in a string with '%20'.
 You may assume that the string has sufficient space at the end to hold the additional characters,
 and that you are given the 'true' length of the string
 (Note: if implementing in java, please use a character array so that you can perform this operation in place)
 DATE: 11/14/2019
"""
import unittest

def p3(str, length):
    str = str.strip()
    str = str.replace(' ', '%20')
    return str

class TestP3(unittest.TestCase):
    def test_p3(self):
        self.assertEqual(p3('Mr John Smith   ', 13), 'Mr%20John%20Smith')
        self.assertEqual(p3('This is a test     ', 14), 'This%20is%20a%20test')
