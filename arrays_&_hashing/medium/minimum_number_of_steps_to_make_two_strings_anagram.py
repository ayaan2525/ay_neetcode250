class Solution(object): 
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        map_s = {}
        map_t = {}
        # Count characters in both strings
        for c in s:
            map_s[c] = map_s.get(c, 0) + 1
        for c in t:
            map_t[c] = map_t.get(c, 0) + 1

        count = 0
        for key in map_s:
            # If the character in s is more than in t, add the difference to count
            # This is the number of steps needed to make the two strings anagrams
            if map_s[key] > map_t.get(key, 0):
                count += map_s[key] - map_t.get(key, 0)

        return count
"""
Question: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
Time Complexity: O(n), where n is the length of s/t.
Space Complexity: O(n + m), for the two dictionaries used to count characters in s and t."""