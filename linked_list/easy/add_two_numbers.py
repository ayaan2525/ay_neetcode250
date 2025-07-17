# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:

            # Get values from the current nodes of l1 and l2, or 0 if they are None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # Calculate sum of the two values and the carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # Return the next node of dummy_head, which is the head of the new linked list
        # This is done to avoid returning the dummy node itself
        return dummy_head.next
    
"""
Question: https://leetcode.com/problems/add-two-numbers/
Time Complexity: O(m, n) where n and m are the lengths of the two linked lists
Space Complexity: O(max(n, m)) for the new linked list
"""