# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # If either tree is empty, return the other tree
        if not root1:
            return root2
        if not root2:
            return root1
        # Create a new tree node with the sum of values from both trees
        merged_tree = TreeNode(root1.val + root2.val)
        # Recursively merge the left and right subtrees
        merged_tree.left = self.mergeTrees(root1.left, root2.left)
        merged_tree.right = self.mergeTrees(root1.right, root2.right)

        return merged_tree
"""
Question: https://leetcode.com/problems/merge-two-binary-trees/
Time Complexity: O(n), where n is the number of nodes in the larger tree.
Space Complexity: O(n), for the recursion stack in the worst case."""
        