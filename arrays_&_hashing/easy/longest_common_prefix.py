from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = min(strs, key=len)
        
        for word in strs:
            # shrink the prefix until it matches the start of the word: e.g. flower and prefix is flowe. it will shrink flowe to flow
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

"""    
Question: https://leetcode.com/problems/longest-common-prefix/
Time complexity: O(n * m), where n is the number of strings and m is the length of the shortest string.
Space complexity: O(1), not using any additional data structures that grow with input size.
""" 