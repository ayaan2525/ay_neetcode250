class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answers = [0] * n
        stack = []
        # Traverse the temperatures in reverse order
        # Using stack to keep track of indices of temperatures
        # that have not found a warmer day yet
        # If the current temperature is warmer than the temperature at the index on top of the stack
        # then we keep popping from the stack until we find a temperature that is warmer
        # If we find such a temperature, we calculate the difference in indices
        # Otherwise, we push the current index onto the stack
        for i in range(n-1,-1,-1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                answers[i] = stack[-1] - i
            stack.append(i)

        return answers
"""
Question: https://leetcode.com/problems/daily-temperatures/
Time Complexity: O(n), where n is the length of temperatures.
Space Complexity: O(n), for the stack used to keep track of indices."""