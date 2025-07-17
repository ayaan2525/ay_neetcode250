# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head

        while current:
            # store the next node 
            temp = current.next
            # reverse the link
            current.next = prev
            # move prev and current one step forward
            prev = current
            # move to the next node
            current = temp
        return prev
        
"""
Question: https://leetcode.com/problems/reverse-linked-list/
Time Complexity: O(n)
Space Complexity: O(1)
"""