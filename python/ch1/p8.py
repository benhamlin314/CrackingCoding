"""
 CREATED BY: Benjamin Hamlin
 Chapter 1 Question 8
 "Zero Matrix"
 PROMPT:
 Write an algorithm such that if an element in an MxN matrix is 0, its entire row
 and column are set to 0.
 DATE: 11/18/2019
"""

import unittest
import numpy

def p8(arr):
    pass

class TestP8(unittest.TestCase):
    def test_p8(self):
        pass

if __name__ == '__main__':
    temp = input("Enter an integer M for the MxN matrix:")
    temp2 = input("Enter an integer N for the NxN matrix:")
    print("Enter each integer of the matrix seperated by a space on a single line:")
    temp2 = list(map(int, input.split()))
    matrix = numpy.array(temp2).reshape(temp, temp2)
    print(p8(matrix))
