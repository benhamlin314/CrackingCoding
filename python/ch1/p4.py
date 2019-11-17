"""
 CREATED BY: Benjamin Hamlin
 Chapter 1 Question 4
 "Palindrom Permutation"
 PROMPT:
 Given a string, write a function to check if it is a permutation of a palindrome.
 a palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
 The palindrome does not need to be limited to just dictionary words.
 You can ignore casing and non-letter characters.
 DATE: 11/16/2019
"""

import unittest

def p4(str):
    str = str.lower()
    str = str.replace(' ', '')
    if (len(str)%2 == 0):
        for letter in str:
            if not (str.count(letter)%2 == 0):
                return False
    else:
        odd = False
        for letter in str:
            if not (str.count(letter)%2 == 0) and odd:
                return False
            elif (str.count(letter)%2 == 1) and not odd:
                odd = True
    return True

class TestP4(unittest.TestCase):
    def test_p4(self):
        self.assertTrue(p4("Taco cat"))
        self.assertTrue(p4("race car"))
        self.assertFalse(p4("buttstuff"))
        self.assertTrue(p4("poopystuffys u"))
