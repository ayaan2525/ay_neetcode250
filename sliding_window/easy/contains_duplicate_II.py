class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        L = 0
        for R in range(len(nums)):
            # maintaing sliding window of size k
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        
        return False
    
    """
    Question: https://leetcode.com/problems/contains-duplicate-ii/
    Time complexity: O(n), where n is the length of nums
    Space Complexity: O(k), k is max size of the sliding window
    """