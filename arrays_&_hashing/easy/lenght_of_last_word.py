class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        i = len(s) - 1
        length = 0
        # Traverse the string from the end to find the last word, 
        # edge case for empty string and single character
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
"""
Question: https://leetcode.com/problems/length-of-last-word/
Time complexity: O(n), where n is the length of the string s
Space complexity: O(1), no extra space used except for variables

"""