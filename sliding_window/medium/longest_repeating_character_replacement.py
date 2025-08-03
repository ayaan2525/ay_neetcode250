class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_char = {}

        left = 0
        res = 0
        maxC = 0

        for right in range(len(s)):

            count_char[s[right]] = 1 + count_char.get(s[right], 0) 
            maxC = max(maxC, count_char[s[right]])

            # Check if window is valid
            if (right - left + 1 )- maxC <= k:
                res = max(res, (right - left + 1))
            # If window is not valid, shrink from the left
            else:
                count_char[s[left]] -= 1
                left += 1
      
        return res

"""
Question: https://leetcode.com/problems/longest-repeating-character-replacement/
Time Complexity: O(n), where n is the length of the string s.
Space Complexity: O(1), since   the size of the count_char dictionary is limited to the number of unique characters in s (which is at most 26 for lowercase English letters).
"""