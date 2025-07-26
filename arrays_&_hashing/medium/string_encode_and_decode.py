class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # Encode the list of strings into a single string
        # Each string is prefixed with its length followed by a '#'
        # This allows us to decode it later by knowing the length of each string
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = j = 0
        while i < len(s):
            j = i
            # Find the next '#' to determine the length of the next string
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            
            # Extract the string of the determined length
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + 1 + length

        return res

"""
Question: https://leetcode.com/problems/encode-and-decode-strings/
Time Complexity: O(n), where n is the total length of all strings in strs.
Space Complexity: O(n), for the encoded string and the list of decoded strings.
"""