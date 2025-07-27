class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dictionary to store the first occurrence of each balance 
        balance_index = {0:-1}
        balance = 0
        max_length = 0

        for i in range(len(nums)):
            # Increment balance for 1 and decrement for 0
            # This way, we can treat 0 as -1 and 1 as +1
            # The balance will be 0 when the number of 0s and 1s are equal
            if nums[i] == 1:
                balance += 1
            else:
                balance -= 1
            # If this balance has been seen before, calculate the length of the subarray
            # from the first occurrence to the current index
            if balance in balance_index:
                length = i - balance_index[balance]
                max_length = max(length, max_length)
            else:
                balance_index[balance] = i
        return max_length
"""
Question: https://leetcode.com/problems/contiguous-array/
Time Complexity: O(n), where n is the length of nums.
Space Complexity: O(n), for the balance_index dictionary 
"""