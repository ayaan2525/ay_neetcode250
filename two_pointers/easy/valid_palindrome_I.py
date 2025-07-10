class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            # Keep skipping non-alphanumeric characters
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            # Compare characters in a case-insensitive manner
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

"""
Question: https://leetcode.com/problems/valid-palindrome
Time complexity: O(n), n is the length of the input string.
Space complexity: O(1), as we are using constant extra space for the two pointers.
"""