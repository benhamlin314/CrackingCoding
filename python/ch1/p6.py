"""
 CREATED BY: Benjamin Hamlin
 Chapter 1 Question 6
 "String Compression"
 PROMPT:
 Implement a method to perform basic string compression using the counts of repeated characters.
 For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would
 not become smaller than the original string, your method should return the original string.
 You can assume the string has only uppercase and lowercase letters.
 DATE: 11/17/2019
"""

import unittest


# O(N)
def p6(str1):
    comp = ""
    prev_letter = str1[0]
    count = 0
    for i in range(0, len(str1)):
        cur_letter = str1[i]
        if prev_letter == cur_letter:
            count += 1
        else:
            comp = comp + prev_letter + str(count)
            prev_letter = cur_letter
            count = 1
    comp = comp + prev_letter + str(count)
    prev_letter = cur_letter
    if len(comp) >= len(str1):
        return str1
    return comp


class TestP6(unittest.TestCase):
    def test_p6_compressed(self):
        self.assertEqual(p6('aabcccccaaa'), 'a2b1c5a3')
        self.assertEqual(p6('bbbbbbcccccccaaaaaatttttfffff'), 'b6c7a6t5f5')

    def test_p6_notCompressed(self):
        self.assertEqual(p6('bbbabcaca'), 'bbbabcaca')


if __name__ == '__main__':
    temp = input("Enter a string to compress:")
    print(p6(temp))
