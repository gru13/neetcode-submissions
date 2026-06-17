class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def solve(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in memo.keys():
                return memo[amount]

            min_coins = float('inf')
            for coin in coins:
                min_coins = min(min_coins, 1 + solve(amount-coin))
            memo[amount] = min_coins
            return min_coins

        result = solve(amount)
        if result == float('inf'):
            return -1
        return result