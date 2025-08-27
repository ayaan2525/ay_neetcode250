class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # handle cases where k is greater than the length of the array
        k = k % len(nums)

        # helper function to reverse a portion of the array
        def reverse(left, right):
            while left < right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1
        # reverse the entire array
        reverse(0, len(nums)-1)

        # reverse the first k elements
        reverse(0, k-1)

        # reverse the remaining elements
        reverse(k, len(nums)-1)

"""
Question: https://leetcode.com/problems/rotate-array/
Time Complexity: O(n)
Space Complexity: O(1)

"""
