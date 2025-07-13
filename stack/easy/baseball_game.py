class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        for ch in ops:
            if ch == "+":
                stack.append(stack[-1] + stack[-2])
            elif ch == "D":
                stack.append(2 * stack[-1])
            elif ch == "C":
                stack.pop()
            else:
                stack.append(int(ch))

        return sum(stack)

"""
Question: https://leetcode.com/problems/baseball-game/
Time complexity: O(n), where n is the length of ops
Space complexity: O(n), in the worst case, all operations are numbers and stored in the stack
"""