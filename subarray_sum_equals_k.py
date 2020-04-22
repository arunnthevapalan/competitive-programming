'''
Problem 22 - 22/02/2020
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {0:1}
        n=len(nums)
        count=0
        s=0
        
        for num in nums:
            s+=num
            if s-k in sum_dict:
                count+= sum_dict[s-k]
            if s in sum_dict:
                sum_dict[s]+=1
            else: sum_dict[s]=1
        
        return count
        
