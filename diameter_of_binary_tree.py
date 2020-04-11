'''
Problem 11 - 11/04/2020
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path (no of edges) between any two nodes in a tree. 
This path may or may not pass through the root.

Example:
          1
         / \
        2   3
       / \     
      4   5   
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
'''
# Approach
# Diameter of a tree is nothing but maximum value of (left_height + right_height + 1) for each node. 
# So we need to calculate (left_height + right_height + 1) for each node and update the result. 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
    
        if root == None:
            return 0
        self.diameter = 0
        
        def height(root: TreeNode, d) -> int:
            if root == None:
                return 0

            left_height = height(root.left, d)
            right_height = height (root.right, d)
            self.diameter = max(self.diameter, left_height+right_height +1)

            return (1 + max(left_height,right_height))
         
        height(root, self.diameter)
        return self.diameter - 1    #edges = nodes - 1
         
