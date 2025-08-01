class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_index = 0
        t_index = 0
        if len(s) == 0:
            return True
        while t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            if s_index == len(s):
                return True
            t_index += 1
        return False
"""
Question: https://leetcode.com/problems/is-subsequence/
Time Complexity: O(n), where n is the length of t.
Space Complexity: O(1), since we are using only a few pointers for index."""