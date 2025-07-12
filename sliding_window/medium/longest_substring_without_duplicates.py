class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = set()
        l, r = 0, 0
        max_length = 0

        for r in range(len(s)):

            # maintain sliding window without duplicates
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            max_length = max(max_length, len(window))
            r += 1
        return max_length
    
    """
    Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    Time complexity: O(n), where n is the length of s
    Space complexity: O(min(m)), m is total unique characters in s, (n:worst case all characters are unique)
    
    """