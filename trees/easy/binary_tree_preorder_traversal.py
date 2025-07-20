# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traverse = []

        def dfs(node):
            if node:
                # Visit the node, then traverse the left subtree, and finally the right subtree
                traverse.append(node.val)
                dfs(node.left)
                dfs(node.right)
            return None
        dfs(root)
        return traverse
    
"""
Question: https://leetcode.com/problems/binary-tree-preorder-traversal/
Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(n), for the recursion stack and the output list.
"""