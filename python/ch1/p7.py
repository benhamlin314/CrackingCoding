"""
 CREATED BY: Benjamin Hamlin
 Chapter 1 Question 7
 "Rotate Matrix"
 PROMPT:
 Given an image represented by an NxN matrix, where each pixel in the image is represented by an integer,
 write a method to rotate the image by 90 degrees. Can you do this in place?
 DATE: 11/18/2019
"""

"""
                      left                right
 1  2  3  4        4  8 12 16           13  9  5  1
 5  6  7  8  ->    3  7 11 12    OR     14 10  6  2
 9 10 11 12        2  6 10 14           15 11  7  3
13 14 15 16        1  5  9 13           16 12  8  4

 1  2  3  4  5      5 10 15 20 25       21 16 11  6  1
 6  7  8  9 10      4  9 14 19 24       22 17 12  7  2
11 12 13 14 15  ->  3  8 13 18 23  OR   23 18 13  8  3
16 17 18 19 20      2  7 12 17 22       24 19 14  9  4
21 22 23 24 25      1  6 11 16 21       25 20 15 10  5
"""

import unittest
import numpy

def p7(arr, dir):
    if dir == 0:
        # rotate right
        temp_int = 0
    else:
        # rotate left
        temp_int = 0

class TestP7(unittest.TestCase):
    def test_p7(self):
        self.assertEqual(p7([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 0), "[[13 9 5 1]\n[14 10 6 2]\n[15 11 7 3]\n[16 12 8 4]]")

if __name__ == '__main__':
    temp = input("Enter an integer N for the NxN matrix representing the image:")
    print("Enter each integer of the matrix seperated by a space on a single line:")
    temp2 = list(map(int, input.split()))
    temp3 = input("Enter 0 to rotate right or 1 to rotate left:")
    matrix = numpy.array(temp2).reshape(temp, temp)
    print(p7(matrix, temp3))
