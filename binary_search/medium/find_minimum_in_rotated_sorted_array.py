class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]: # discard left, as minimum must be to the right
                l = mid + 1
            else:
                r = mid # discard right, as minimum must be to the left or at mid
        return nums[l]

        