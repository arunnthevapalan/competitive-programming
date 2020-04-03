'''
Problem 03 - 03/04/2020
Given an integer array nums, find the contiguous subarray (containing at least one number),
which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach.
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = nums[0]
        local_sum = nums[0]
        for num in nums[1:]:
            local_sum = max(num, local_sum+num)
            global_sum = max(local_sum, global_sum)
        return global_sum
        
