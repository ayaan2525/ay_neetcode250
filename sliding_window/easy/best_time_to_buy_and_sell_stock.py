class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        maxProfit = 0

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxProfit
        
"""
Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Time complexity: O(n), where n is the length of prices
Space complexity: O(1), no extra space used
"""