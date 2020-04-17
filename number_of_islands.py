'''
Problem 17 - 17/04/2020
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11000
11000
00100
00011

Output: 3
'''
#classic question, run a DFS to find the number of connected components
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                if (grid[i][j] == "1"):
                    grid[i][j] = "0"
                    
                    dfs(i+1, j)
                    dfs(i, j+1)
                    dfs(i-1, j)
                    dfs(i, j-1)
                    return True
            return False
        
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i, j):
                    islands +=1
        return islands
        
