class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = float('inf')
        for a in prices:
            if a < min_value:
                min_value = a
            max_profit = max(max_profit, a-min_value)
        return max_profit