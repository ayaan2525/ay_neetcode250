# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
"""
Question: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: Balanced Tree: O(log n), worst case O(n) for skewed trees, due to recursion stack.
"""