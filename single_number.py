# Problem 01 - 01/04/2020
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result = result ^ i
            
        return result
        
        
