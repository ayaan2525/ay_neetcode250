# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # Helper function to check if two trees are the same
        def isSameTree(p,q) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    
        if not root:
            return False
        # Check if the current node matches the root of the subtree
        if isSameTree(root, subRoot):
                    return True
        # Recursively check the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
"""Question: https://leetcode.com/problems/subtree-of-another-tree/
Time Complexity: O(m * n), where m is the number of nodes in the main tree and n is the number of nodes in the subtree.
Space Complexity: O(m + n), for the recursion stack and the space used by the isSameTree function.
"""