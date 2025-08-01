"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        def postorder_dfs(node):
            if not node:
                return
            # Traverse all children first 
            for children in node.children:
                postorder_dfs(children)
            # Then visit the node itself
            result.append(node.val)
        postorder_dfs(root)
        return result
"""
Question: https://leetcode.com/problems/n-ary-tree-postorder-traversal/
Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(n), for the recursion stack and the output list
Try to use iterative approach as well.
"""