# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            # If left or right subtree is unbalanced, propagate -1 up
            # to indicate the tree is unbalanced
            if left == -1:
                return -1
            if right  == -1:
                return -1
            
            # If the difference in heights is more than 1, return -1
            # to indicate the tree is unbalanced other return height of the current tree
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
        
        return dfs(root) != -1
        
"""
Question: https://leetcode.com/problems/balanced-binary-tree/
Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(n), for the recursion stack.
"""