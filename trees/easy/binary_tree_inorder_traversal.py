# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traverse = []
        # helper function to perform DFS
        def dfs(node):
            if node:
                # Traverse the left subtree, visit the node, then traverse the right subtree
                dfs(node.left)
                traverse.append(node.val)
                dfs(node.right)
        dfs(root)
        return traverse

"""
Question: https://leetcode.com/problems/binary-tree-inorder-traversal/
Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(n), for the recursion stack and the output list.
"""