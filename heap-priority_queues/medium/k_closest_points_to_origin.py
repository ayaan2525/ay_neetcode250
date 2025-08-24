import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        k_closest = []
        result = []

        for point in points:

            # calculae the distance from origin
            current_dist = (point[0]**2 + point[1]**2) ** 0.5

            # use a max-heap to keep track of k closest points
            if len(k_closest) < k:
                heapq.heappush(k_closest, (-current_dist, point))
            else:

                # if the current point is closer than the farthest, replace it,
                # first it pushes the new point and then pops the farthest
                heapq.heappushpop(k_closest, (-current_dist, point))

        # extract and return the points from the heap
        while len(k_closest):
            result.append(heapq.heappop(k_closest)[1])
        return result

        