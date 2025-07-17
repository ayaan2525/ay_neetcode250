# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = node = ListNode()
        # dummy node to simplify the merging process   
        # Iterate through both lists and merge them
        # based on the values of the nodes
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next =  list2
                list2 = list2.next
            node = node.next

        node.next = list1 if list1 else list2
        return newHead.next
        
"""
Question: https://leetcode.com/problems/merge-two-sorted-lists/
Time Complexity: O(n + m) where n and m are the lengths of the two lists
Space Complexity: O(1)
"""