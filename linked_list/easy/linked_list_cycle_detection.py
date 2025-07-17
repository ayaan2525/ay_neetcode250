# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # Use two pointers, slow and fast
        # If there is a cycle, they will meet at some point
        # If there is no cycle, fast will reach the end of the list 
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
"""
Question: https://leetcode.com/problems/linked-list-cycle/
Time Complexity: O(n)   
Space Complexity: O(1)
"""            