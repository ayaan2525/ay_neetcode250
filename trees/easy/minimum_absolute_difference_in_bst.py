# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root) -> int:
        
        self.prev = None
        self.minimum = float('inf')

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            # If this is not the first node, calculate the difference
            # and update the minimum difference if necessary
            # Update the previous node value to the current node value
            # This ensures that we always have the previous node value for comparison
            if self.prev != None:
                self.minimum = min(self.minimum, abs(self.prev - node.val))
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.minimum
"""
Question: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(h), where h is the height of the tree, due to recursion stack.
"""