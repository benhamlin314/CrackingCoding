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
 5  6  7  8  ->    3  7 11 15    OR     14 10  6  2
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

# O(n^3) where n is the size of the NxN matrix
def p7_copy(arr, dir):
    cp = []
    for i in range(0, len(arr)):
        temp_arr = []
        for j in range(0, len(arr)):
            temp_arr.append(arr[j][i])
        if dir == 0:
            # rotate right
            temp_arr.reverse()# O(N)
            cp.append(temp_arr)
        else:
            # rotate left
            cp.append(temp_arr)
    if dir == 1:# negligible in time complexity compared to the rest
        cp.reverse()
    return cp

def p7_inplace(arr, dir):
    if dir == 0:
        # rotate right
        temp_int = 0
    else:
        # rotate left
        temp_int = 0
    return arr
    
"""
def p7_copy(arr, dir):
    if dir == 0:
        # rotate right
        for r in range(len(arr)):
            for c in range(len(r)):
                pass
    else:
        # rotate left
        temp_int = 0
    return arr
"""

class TestP7(unittest.TestCase):
    def test_p7_copy_4x4(self):
        self.assertEqual(p7_copy([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 0),
            [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]])
        self.assertEqual(p7_copy([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 1),
            [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]])

    def test_p7_copy_5x5(self):
        self.assertEqual(p7_copy([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 1),
            [[5, 10, 15, 20, 25], [4, 9, 14, 19, 24], [3, 8, 13, 18, 23], [2, 7, 12, 17, 22], [1, 6, 11, 16, 21]])
        self.assertEqual(p7_copy([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 0),
            [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]])

    @unittest.skip("inplace not implemented yet")
    def test_p7_inplace_4x4(self):
        self.assertEqual(p7_copy([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 0),
            [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]])
        self.assertEqual(p7_copy([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 1),
            [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]])

    @unittest.skip("inplace not implemented yet")
    def test_p7_inplace_5x5(self):
        self.assertEqual(p7_copy([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 1),
            [[5, 10, 15, 20, 25], [4, 9, 14, 19, 24], [3, 8, 13, 18, 23], [2, 7, 12, 17, 22], [1, 6, 11, 16, 21]])
        self.assertEqual(p7_copy([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 0),
            [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]])

if __name__ == '__main__':
    temp = input("Enter an integer N for the NxN matrix representing the image:")
    print("Enter each integer of the matrix seperated by a space on a single line:")
    temp2 = list(map(int, input.split()))
    temp3 = input("Enter 0 to rotate right or 1 to rotate left:")
    matrix = numpy.array(temp2).reshape(temp, temp)
    print(p7_copy(matrix, temp3))
    print(p7_inplace(matrix, temp3))
