'''
Problem 27 - 27/04/2020
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        mat2 = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                mat2[i][j] = min(mat2[i - 1][j - 1], mat2[i - 1][j], mat2[i][j - 1]) + 1 if matrix[i][j] == '1' else 0
        return max([max(row) for row in mat2]) ** 2
