class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a, b = 0, 1
        maxp = 0
        while b<len(prices):
            if prices[a] < prices[b]:
                maxp = max(maxp, prices[b] - prices[a])
            else:
                a = b
            b += 1
        return maxp
