'''
Problem 18 - 18/04/2020
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which 
minimizes the sum of all numbers along its path. You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
#Approach, dynammic programming. Fill an array finding the min path for every cell.
#https://www.youtube.com/watch?v=ItjZdu6jEMs

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m >0 else 0
        if m==0 or n==0:
            return 0
        
        dp = [ [ 0 for i in range(n) ] for j in range(m) ] 
        for i in range(m):
            for j in range(n):
                dp [i][j] += grid[i][j]
                if (i>0 and j>0):
                    dp[i][j]+=min(dp[i-1][j],dp[i][j-1])
                elif (i>0):
                    dp[i][j]+=dp[i-1][j]
                elif (j>0):
                    dp[i][j]+=dp[i][j-1]
                
        return dp[m-1][n-1]
        
