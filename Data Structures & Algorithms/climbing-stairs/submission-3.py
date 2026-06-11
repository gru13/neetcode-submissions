class Solution:

    def climbStairs(self, n: int) -> int:
        memo = {}
        def solve(n):
            if n<=2:
                return n
            if n in memo:
                return memo[n]
            result =  solve(n-1)+solve(n-2)   
            memo[n] = result
            return result
        return solve(n) 