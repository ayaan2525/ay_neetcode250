class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n -1
        k = m + n - 1

        while j >= 0:
            # Fill nums1 from the end until all elements of nums2 are merged
            if  i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1        

"""
Question: https://leetcode.com/problems/merge-sorted-array
Time complexity: O(m + n), where m is the length of nums1 and n is the length of nums2.
Space complexity: O(1), as we are modifying nums1 in place
"""