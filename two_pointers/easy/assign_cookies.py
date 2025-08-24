"""
import heapq
class Solution(object):
    def findContentChildren(self, g, s):
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        # HEAP SOLUTION
        # Min-heap to efficiently get the smallest greed factor and cookie size
        heapq.heapify(g)
        heapq.heapify(s)
        
        count = 0
        while len(g) > 0 and len(s) > 0:

            # get the child with the smallest greed factor
            child = heapq.heappop(g)

            # find a cookie that can satisfy this child
            while len(s) > 0:      
                cookie = heapq.heappop(s)
                if cookie >= child:
                    count += 1
                    break
        return count
"""

# TWO POINTERS SOLUTION
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # Sort both lists to use two pointers
        g.sort()
        s.sort()
        count = 0
        # initialize two pointers for greed and cookie factors
        greed, cookie = 0, 0
        while greed < len(g) and cookie < len(s):
            
            # if the current cookie can satisfy the current child, incremen count
            if s[cookie] >= g[greed]:
                
                count += 1
                greed += 1
            cookie += 1
        return count

"""
Question: https://leetcode.com/problems/assign-cookies/
Time Complexity: O(n log n + m log m), where n is the length of g and m is the length of s, due to sorting.
Space Complexity: O(1), no extra space used
"""
