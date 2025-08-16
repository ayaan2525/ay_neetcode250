import heapq, math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        heap = []
        # use max-heap by pushing negative values
        for i in gifts:
            heapq.heappush(heap, -i)
        while k > 0:
            gift = heapq.heappop(heap)
            # take the square root of the largest gift and push it back
            heapq.heappush(heap, int(-(-gift)**0.5))
            k -= 1
        
        result = 0
        for i in heap:
            result += (-i)
        return int(result)

"""
Question: https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/
Time Complexity: O(n + k log n) where n is the number of gifts and k is the number of operations.
Space Complexity: O(n) for the heap storage.
"""