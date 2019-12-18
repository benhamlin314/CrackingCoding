"""
 CREATED BY: Benjamin Hamlin
 Chapter 1 Question 2
 "Check Permutation"
 PROMPT:
 Given two stings, write a method to decide if one is a permutation of the other
 DATE: 11/14/2019
"""
import unittest

# O(N) where N is the length of str1
# O(1) when strings are not the same length


def p2(str1, str2):
    if len(str1) == len(str2):
        for letter in str1:
            if str1.count(letter) != str2.count(letter):
                return False
        return True
    else:
        return False


class TestP2(unittest.TestCase):
    def test_p2(self):
        self.assertTrue(p2("cat", "tac"))
        self.assertTrue(p2("own", "won"))
        self.assertFalse(p2("chicken", "butt"))


if __name__ == '__main__':
    temp = input("Enter a string:")
    temp2 = input("Enter a string to see if it is a permutation of the other:")
    print(p2(temp, temp2))
