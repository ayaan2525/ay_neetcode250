class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        first_pointer = 0
        second_pointer = 1
        k = 1
        while second_pointer < len(nums):
            if nums[first_pointer] == nums[second_pointer]:
                second_pointer += 1
            else:
                first_pointer += 1
                nums[first_pointer] = nums[second_pointer]
                second_pointer += 1
                k += 1
        return k

"""
Question: https://leetcode.com/problems/remove-duplicates-from-sorted-array
Time complexity: O(n), where n is the length of the input list.
Space complexity: O(1), no extra space is used, modifying input list in place.
"""



        