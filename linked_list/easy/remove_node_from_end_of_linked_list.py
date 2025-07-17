# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        # Calculate the length of the linked list
        # to find the nth node from the end
        while current != None:
            length += 1
            current = current.next

        # if n is equal to length, remove head and return the next node
        if n == length:
            return head.next

        # Find the node before the nth node from the end
        step_to_prev = length - n - 1
        current = head
        while step_to_prev > 0:
            step_to_prev = step_to_prev - 1
            current = current.next
        current.next = current.next.next
        return head
