# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root, targetSum):
            if not root:
                return False
            # If we reach a leaf node, check if the path sum equals targetSum
            if root.left == None and root.right == None:
                return targetSum == root.val
            # subtract current node's val from targetSum and continue to left and right child
            targetSum -= root.val
            return dfs(root.left, targetSum) or dfs(root.right, targetSum)
        return dfs(root, targetSum)
"""
Question: https://leetcode.com/problems/path-sum/
Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(h), where h is the height of the tree, due to the recursion stack.
"""