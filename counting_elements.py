'''
Problem 07 - 07/04/2020
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.

Examples:
Input: arr = [1,2,3]          Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Input: arr = [1,3,2,3,5,0]    Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

Input: arr = [1,1,2,2]        Output: 2
Explanation: Two 1s are counted cause 2 is in arr.
'''

#Approach 1 using membership function
class Solution:
    def countElements(self, arr: List[int]) -> int:
        count =0
        for num in arr:
            if num+1 in arr:
            count+=1
        return count

#Approach 2 without searching    
class Solution:
    def countElements(self, arr: List[int]) -> int:
        count =0
        temp = 0
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                temp+=1
            elif arr[i]+1==arr[i+1]:
                count=count + temp + 1
                temp = 0
            else: temp =0
        return count
