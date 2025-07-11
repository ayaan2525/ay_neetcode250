class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]
            # if current sum is greater than target, move right pointer left
            if curSum > target:
                r -= 1
            # if current sum is less than target, move left pointer right
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []
        
        
"""
Question: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
Time complexity: O(n), where n is the length of the input list.
Space complexity: O(1), no extra data scructure used
"""