class Solution:
    def mergeAlternatvely(self, word1: str, word2: str) -> str:
        merged = []
        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            merged.append(word1[i])
            merged.append(word2[i])

        merged.append(word1[min_len:])
        merged.append(word2[min_len:])

        return "".join(merged)
    
"""
Question: https://leetcode.com/problems/merge-strings-alternately
Time complexity: O(n+m),
Space complexity: O(n+m)
"""