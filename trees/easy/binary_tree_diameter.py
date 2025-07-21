# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        # The diameter is the longest path between any two nodes in the tree,
        # path may or may not pass through the root node
        # The function returns the height of the current node
        # while updating the diameter at each node
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, left + right)

            return 1 + max(left, right)
        dfs(root)
        return res

"""
Question: https://leetcode.com/problems/diameter-of-binary-tree/
Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(n), for the recursion stack."""        