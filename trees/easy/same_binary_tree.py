# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if both nodes are None
        # If both are None, empty: return True
        # If one is None and the other is not, they are not the same tree: return False
        # If both are not None, check their values and recursively check their left and right subtrees
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
"""
Question: https://leetcode.com/problems/same-tree/
Time Complexity: O(n), where n is the number of nodes in the trees.
Space Complexity: O(n), for the recursion stack.

"""