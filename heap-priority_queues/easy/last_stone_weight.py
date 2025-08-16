import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap_stones = []

        # use max-heap by pushing negative values
        for i in stones:
            heapq.heappush(heap_stones, -i)
        
        while len(heap_stones) > 1: 
            x = -heapq.heappop(heap_stones)
            y = -heapq.heappop(heap_stones)

            # if difference is non-zero, push it back
            diff = -abs(x-y)
            if diff:
                heapq.heappush(heap_stones, diff)  
        # if last two stones are equal, return 0 else return the last remaining stone
        return -heap_stones[0] if heap_stones else 0
