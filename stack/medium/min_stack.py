class MinStack(object):

    def __init__(self):
        self.arr = []
        self.minarr = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.arr.append(val)
        if len(self.minarr) == 0:
            self.minarr.append(val)
        else:
        # If the new value is less than or equal to the current minimum, update the minimum stack
        # this ensures that the minimum stack always has the minimum value at the top
            self.minarr.append(min(val, self.minarr[-1]))
    def pop(self):
        """
        :rtype: None
        """
        self.arr.pop()
        self.minarr.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minarr[-1]
"""
Question: https://leetcode.com/problems/min-stack/
Time Complexity: O(1) for push, pop, top, and getMin operations.
Space Complexity: O(n), where n is the number of elements in the stack."""