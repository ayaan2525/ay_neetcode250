class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen  = ()
        while n != 1:
            nums = 0
            current = n
            while current > 0:
                digit += n % 10
                nums += digit ** 2
                current = current // 10

            if nums in seen:
                return False
            seen.add(nums)
            n = nums
        return True
"""
Question: https://leetcode.com/problems/happy-number/
Time Complexity: O(log n), where n is the number of digits in the number.
Space Complexity: O(log n), for the seen set which stores intermediate sums.
"""
        
        