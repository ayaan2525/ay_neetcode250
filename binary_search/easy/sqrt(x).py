class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l <= r:
            mid = (l+r) // 2
            if (mid * mid) == x:
                return mid
            elif (mid * mid) > x:
                r = mid - 1
            
            else:
                l = mid + 1
        # When the loop ends, l is the first number whose square is greater than x
        # Therefore, the largest integer whose square is less than or equal to x is l -
        return l - 1
        
"""
Question: https://leetcode.com/problems/sqrtx/
Time complexity: O(log n), binary search 
Space complexity: O(1), no extra space is used
"""