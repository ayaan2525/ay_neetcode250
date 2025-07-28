class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        max_len = 0
        # Iterate through each number
        # If the number is the start of a sequence (i.e., i-1 is not in the set),
        # then count the length of the sequence starting from that number
        # This ensures we only count each sequence once
        for i in nums:
            curr_len = 1
            if i-1 in nums_set:
                seq = i
                while seq in nums_set:
                    curr_len += 1
                    seq = seq + 1
            max_len = max(curr_len, max_len)
            
        
        return max_len
    
"""
Question: https://leetcode.com/problems/longest-consecutive-sequence/
Time Complexity: O(n), where n is the number of elements in nums.
Space Complexity: O(n), for the set used to store the elements of nums.
"""