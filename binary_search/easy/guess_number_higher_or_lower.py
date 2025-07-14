# The guess API is already defined in leetcode.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:
            mid = (l + r) // 2
            # Using the guess API to determine if the guess is too high, too low, or correct
            if guess(mid) == -1:
                r = mid - 1
            elif guess(mid) == 1:
                l = mid + 1
            else:
                return mid
        return mid
"""
Question: https://leetcode.com/problems/guess-number-higher-or-lower/
Time complexity: O(log n), we are using binary search 
Space complexity: O(1), no extra space is used
"""
        