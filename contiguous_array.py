'''
Problem 13 - 13/04/2020
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

Example
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''
#Correct brute-force solution, however time-limit exceeded. To be optimized.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        start = 0
        end = 0
        max_len = 0
        for start in range(len(nums)+1):
            for end in range(start,len(nums)+1):
                if nums[start:end].count(1)==nums[start:end].count(0):
                    max_len = max(max_len, (end-start))
        return max_len
                
            
        
        
