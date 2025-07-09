class Solution:
    def reverseString(self, s: List[str]) -> None:
    
        # This function reverses the input list of characters in place.
        temp = ""
        start = 0
        end = len(s) - 1
        while start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1

"""
Question: https://leetcode.com/problems/reverse-string
Time complexity: O(n), where n is the length of the input list.
Space complexity: O(1), as we are using a constant amount of extra space for the temporary variable.        # Time complexity: O(n), where n is the length of the input list.
""" 