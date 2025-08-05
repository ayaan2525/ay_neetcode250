# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Function to reverse the linked list
    def reverse(self, node: Optional[ListNode]) -> ListNode:
        current = node
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:

        # if the list is empty or has less than 3 nodes, no reordering is needed
        if not head or not head.next or not head.next.next:
            return
        # find the middle of the linked list 
        slow, fast = head,head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # disconnect the first half from the second half
        prev.next = None
        
        l1 = head
        # reverse the second half of the linked list
        l2 = self.reverse(slow)

        # merge the two halves l1: first half, l2: reversed second half
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            if l1_next is None:
                break
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next
        

"""
Question: https://leetcode.com/problems/reorder-list/
Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(1), no extra space is used.
"""
        