from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Frequency map to count occurrences of each number
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        # Create buckets where index represents frequency
        # and each bucket contains numbers with that frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, frequency in freq_map.items():
            buckets[frequency].append(key)

        result = []
        # Iterate from end(highest frequency and go downwards) of the buckets to get the most frequent elements
        # ensuring we get the top k elements in descending order of frequency
        # until we have collected k elements
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:git 
                    return result

"""
Question: https://leetcode.com/problems/top-k-frequent-elements/
Time Complexity: O(n), where n is the length of nums.
Space Complexity: O(n), for the frequency map and buckets.

"""
