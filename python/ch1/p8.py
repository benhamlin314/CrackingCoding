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

# O(N*M)
def p8(arr):
    zeros = []
    rows = len(arr)
    cols = len(arr[0])
    for r in range(rows):
        for c in range(cols):
            if arr[r][c] == 0:
                zeros.append([r,c])
    for x, y in zeros:
        for i in range(rows):
            arr[i][y] = 0
        for i in range(cols):
            arr[x][i] = 0
    return arr

class TestP8(unittest.TestCase):
    def test_p8_small(self):
        self.assertEqual(p8([[1,0],[1,2]]), [[0, 0], [1, 0]])
    def test_p8_medium(self):
        self.assertEqual(p8([[1,2,0,0],[3,2,4,1],[0,2,3,1]]), [[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0]])
    def test_p8_large(self):
        self.assertEqual(p8([[1,1,1,1,1,1],[0,1,2,3,4,4],[2,3,4,2,0,1],[1,2,3,4,2,4],[1,0,1,3,4,5]]), [[0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 3, 4, 0, 4], [0, 0, 0, 0, 0, 0]])

if __name__ == '__main__':
    temp = input("Enter an integer M for the MxN matrix:")
    temp2 = input("Enter an integer N for the NxN matrix:")
    print("Enter each integer of the matrix seperated by a space on a single line:")
    temp2 = list(map(int, input.split()))
    matrix = numpy.array(temp2).reshape(temp, temp2)
    print(p8(matrix))
