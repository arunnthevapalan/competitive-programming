'''
Problem 30 - 30/04/2020
Given a binary tree where each path going from the root to any leaf form a valid sequence,
check if a given string is a valid sequence in such binary tree. 
We get the given string from the concatenation of an array of integers arr and the concatenation 
of all values of the nodes along a path results in a sequence in the given binary tree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        l = len(arr)
        i =0
        return self.checkpath(root, arr, l, i)
    
    def checkpath(self, root, arr, l, i):
        if root is None:
            return l==0
        if (i==l-1) and (root.left == None and root.right==None) and (root.val == arr[i]):
            return True
        
        if (i<l) and (root.val ==arr[i]):
            return self.checkpath(root.left, arr,l, i+1) or self.checkpath(root.right, arr, l, i+1)
