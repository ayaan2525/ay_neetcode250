import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.minheap, self.k = nums, k
        heapq.heapify(self.minheap)
        # Ensure the heap only contains the k largest elements
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)

        # If the heap exceeds size k, remove the smallest element
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]


"""
Question: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Time Complexity: O(n log k) for initialization, m add operations take O(log k) each
Space Complexity: O(k) for the min-heap
"""