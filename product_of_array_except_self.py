'''
Problem 15 - 15/04/2020
Given an array nums of n integers where n > 1,  return an array output such that 
output[i] is equal to the product of all the elements of nums except nums[i].
Please solve it without division and in O(n).
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array 
            (including the whole array) fits in a 32 bit integer.
Follow up: Could you solve it with constant space complexity? (The output array does not count as extra space)

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
'''

#Approach [a1,a2,a3,a4,a5] = [1,a1,a1a2,a1a2a3,a1a2a3a4] * [a5a4a3a2,a5a4a3,a5a4,a5,1]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:         
        product=1
        result=[1]*len(nums)
        
        for i in range(len(nums)-1):
            result[i+1] =  result[i] *nums[i]
        
        for j in range(len(nums)-1,0,-1):
            product =  product * nums[j]
            result[j-1] = product * result[j-1]
        return result
