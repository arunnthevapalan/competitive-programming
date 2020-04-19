'''
Problem 19 - 19/04/2020
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''
#Approach can be improved to search and find pivot in same loop
#https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot(arr, low, high): 
            # base cases 
            if high < low: 
                return -1
            if high == low: 
                return low 

            #low + (high - low)/2; 
            mid = int((low + high)/2) 

            if mid < high and arr[mid] > arr[mid + 1]: 
                return mid 
            if mid > low and arr[mid] < arr[mid - 1]: 
                return (mid-1) 
            if arr[low] >= arr[mid]: 
                return findPivot(arr, low, mid-1) 
            return findPivot(arr, mid + 1, high) 
            
        def binarySearch(arr, low, high, key):
            if high < low: 
                return -1

            #low + (high - low)/2;     
            mid = int((low + high)/2) 

            if key == arr[mid]: 
                return mid 
            if key > arr[mid]: 
                return binarySearch(arr, (mid + 1), high, 
                                                    key); 
            return binarySearch(arr, low, (mid -1), key); 
            
        pivot = findPivot(nums, 0 , len(nums)-1)
        if pivot == -1:
            return binarySearch(nums, 0, len(nums)-1, target)
        if nums[pivot] == target:
            return pivot
        if nums[0] <= target:
            return binarySearch(nums, 0, pivot-1, target)
        else: return binarySearch(nums, pivot+1, len(nums)-1, target)
