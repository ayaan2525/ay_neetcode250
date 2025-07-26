from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Count occurrences of each color (0, 1, 2)
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        index = 0
        for key in range(3):
            value = count.get(key)
            # If the color is not present, continue to the next key
            if value == None:
                continue
            # Fill the nums array with the current color
            while value > 0:
                nums[index] = key
                value -= 1
                index += 1
"""
Question: https://leetcode.com/problems/sort-colors/
Time Complexity: O(n), where n is the length of nums.
Space Complexity: O(1), since we are using a fixed-size count array for colors

"""
