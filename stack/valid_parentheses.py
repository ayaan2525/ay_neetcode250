class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")":"(", "}":"{", "]":"[" }

        for ch in s:
            if ch in ["(", "{", "["]:
                stack.append(ch)
            # If the current character is a closing parenthesis
            # check if the stack is not empty and the top of the stack matches the corresponding opening parenthesis
            elif len(stack) > 0 and stack[-1] == pair[ch]:
                stack.pop()
            else:
                return False
        # If stack is empty, all parentheses are matched
        return not stack
    
"""
Question: https://leetcode.com/problems/valid-parentheses/
Time complexity: O(n), where n is the length of s
Space complexity: O(n), in the worst case, all characters are opening parentheses and stored in
"""
