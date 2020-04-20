'''
Problem 20 - 20/04/2020
Return the root node of a binary search tree that matches the given preorder traversal.
Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, 
and any descendant of node.right has a value > node.val. Also recall that a preorder traversal displays the value of the node 
first, then traverses node.left, then traverses node.right.)
Note:
      1 <= preorder.length <= 100
      The values of preorder are distinct.

Example:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Approach 1
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i<len(preorder) and  preorder[i] < root.val:
            i+=1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
 
 #Approach 2
 class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return
    
        root = TreeNode(preorder[0])
        
        def insert(val, root):
            # we insert a single element using this function
            
            while True:
                # Here we check whether root's value is greater than the given value.
                # If yes then try to insert it in the left sub-tree.
                if root.val > val:
                    # Here we check if the left child does not exist then we add a left child with value = val and break the loop
                    if not root.left:
                        root.left = TreeNode(val)
                        break
                     # Since the left child exists we move towards the left.
                    else:
                        root = root.left
                # This will work similar to the left child.
                else:
                    if not root.right:
                        root.right = TreeNode(val)
                        break
                    else:
                        root = root.right
        head = root       
        for i in range(1, len(preorder)):
            # Here we reset the head pointer so we are the top of the tree again.
            head = root
            insert(preorder[i], head)
        
        return head
