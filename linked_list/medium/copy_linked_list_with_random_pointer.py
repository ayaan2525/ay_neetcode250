"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Create a mapping from original nodes to copied nodes
        # This will help in setting the random pointers correctly
        original_to_copy = {}
        current = head

        # First pass: create a copy of each node without random pointers
        while current != None:
            original_to_copy[current] = Node(current.val)
            current = current.next
        
        # Second pass: set the next and random pointers for the copied nodes
        new_head = Node(0)
        new_current = new_head
        current = head

        while current:
            # Set the next pointer for the copied node
            copied_node = original_to_copy[current]
            new_current.next = copied_node
            # Set the random pointer for the copied node
            new_current.next.random = original_to_copy.get(current.random)
            current = current.next
            new_current = new_current.next
        return new_head.next



"""
Question: https://leetcode.com/problems/copy-list-with-random-pointer/
Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(n), where n is the number of nodes in the linked list
"""