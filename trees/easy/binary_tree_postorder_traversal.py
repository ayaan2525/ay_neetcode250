# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traverse = []
        
        def dfs(node):
            if node:
                # Traverse the left subtree, then the right subtree, and finally visit the node
                dfs(node.left)
                dfs(node.right)
                traverse.append(node.val)
            return None
        dfs(root)
        return traverse
"""
Question: https://leetcode.com/problems/binary-tree-postorder-traversal/
Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(n), for the recursion stack and the output list. 
"""