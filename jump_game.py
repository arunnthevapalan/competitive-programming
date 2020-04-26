'''
Problem 25 -26/04/2020
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example: 
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums)-1      
        for i in range(len(nums)-2,-1,-1): # Iterate backwards from second to last item until the first item
            if (i + nums[i]) >= last_position: # If this index has jump count which can reach to or beyond the last position
                last_position = i # Since we just need to reach to this new index
        return last_position == 0	
