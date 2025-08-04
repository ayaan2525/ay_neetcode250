class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i in range(len(nums)):

            # If the current number is greater than 0, break the loop
            # since all subsequent numbers will also be greater than 0,
            if nums[i] > 0:
                break
            # skip duplicates to avoid repeated triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            # Use two pointers to find pairs that sum to the negative of the current number
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicates for the second number
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return res
"""
Question: https://leetcode.com/problems/3sum/
Time Complexity: O(n^2), where n is the length of the input list nums.
Space Complexity: O(1)/O(n), depends on sorting algorithm. O(m) for output list
"""



        