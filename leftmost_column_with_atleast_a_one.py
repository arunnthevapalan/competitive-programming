'''
Problem 21 - 21/04/2020
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, 
this row is sorted in non-decreasing order. Given a row-sorted binary matrix binaryMatrix, 
return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:
      BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
      BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  
Also, any solutions that attempt to circumvent the judge will result in disqualification.

Example:
Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
'''
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        current_row = 0
        current_col = cols-1
        while (current_row<rows and current_col >=0):
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row+=1
            else: current_col -=1
        
        if current_col != cols-1:
            return current_col+1
        else: return -1
