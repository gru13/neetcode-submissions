class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for (i, a) in enumerate(prices):
            for j in range(i+1, len(prices)):
                maxP = max(maxP, prices[j] - a)
        return maxP