# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root: return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
"""
Question: https://leetcode.com/problems/invert-binary-tree/
Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(n), due to recursion stack."""