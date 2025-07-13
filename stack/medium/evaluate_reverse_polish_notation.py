class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  
        for i in tokens:
            if i.lstrip('-').isdigit():  # Also handles negative numbers
                stack.append(int(i))
            elif i == "+":
                ele1 = stack.pop()
                ele2 = stack.pop()
                stack.append(ele2 + ele1)
            elif i == "-":
                ele1 = stack.pop()
                ele2 = stack.pop()
                stack.append(ele2 - ele1)
            elif i == "*":
                ele1 = stack.pop()
                ele2 = stack.pop()
                stack.append(ele2 * ele1)
            else:  # Division
                ele1 = stack.pop()
                ele2 = stack.pop()
                stack.append(int(ele2 / ele1))  # Truncate toward zero

        return stack[0]
"""
Question: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Time complexity: O(n), where n is the number of tokens
Space complexity: O(n), in the worst case, all tokens are numbers and stored in the stack
"""
