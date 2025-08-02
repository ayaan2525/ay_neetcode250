# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """    
        def divide_conquer(arr):
            
            # Base case: if the array is empty, return None
            if not arr:
                return None
            # find mid and make it the root
            mid = len(arr) // 2
            node = TreeNode(arr[mid])

            # Recursively build the left and right subtrees
            node.left = divide_conquer(arr[:mid])
            node.right = divide_conquer(arr[mid+1:])

            return node

        return divide_conquer(nums)
"""

Question: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Time Complexity: O(n), where n is the number of elements in the input array.
Space Complexity: O(n), due to the recursion stack and the tree structure."""