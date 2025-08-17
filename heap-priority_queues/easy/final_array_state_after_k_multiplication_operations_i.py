import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        # min-heap to keep track of the smallest elements, 
        # using tuple to compare indices if values are equal
        res = nums
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        
        while k > 0:
            num, i = heapq.heappop(heap)
            res[i] = num * multiplier
            heapq.heappush(heap, (num*multiplier, i))

            k -= 1
        return res

"""
Question: https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/
Time Complexity: O(n + k log n), n is the number of elements in nums and k is the number of operations.
Space Complexity: O(n) for the heap storage.
"""