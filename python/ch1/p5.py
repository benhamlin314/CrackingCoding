"""
 CREATED BY: Benjamin Hamlin
 Chapter 1 Question 5
 "One Away"
 PROMPT:
 There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
 Given two strings, write function to check if they are one edit (or zero edits) away.
 DATE: 11/16/2019
"""

import unittest

def checkInsert(str1, str2):
    if len(str1) > len(str2):
        for i in range(0,len(str2)):
            if str1[i] != str2[i]:
                str3 = str2[:i] + str1[i] + str2[i:]
                break
        if str1 == str3:
            return True
        else:
            return False
    else:
        for i in range(0,len(str1)):
            if str1[i] != str2[i]:
                str3 = str1[:i] + str2[i] + str1[i:]
                break
        if str3 == str2:
            return True
        else:
            return False

def checkReplace(str1, str2):
    pass

def checkRemove(str1, str2):
    pass

def p5(str1, str2):
    if len(str1) == len(str2):
        if checkReplace(str1, str2):
            return True
    else:
        if checkInsert(str1, str2):
            return True
        else:
            if checkRemove(str1, str2):
                return True
    return False

class TestP5(unittest.TestCase):
    def test_p5(self):
        self.assertTrue(p5("pale", "ple"))
        self.assertTrue(p5("pales", "pale"))
        self.assertTrue(p5("pale", "bale"))
        self.assertFalse(p5("pale", "bake"))
