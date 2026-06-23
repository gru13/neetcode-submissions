class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        def solve(i,j):
            if (i == m - 1 and j == n - 1):
                return 1

            if i >= m or j >= n:
                return 0

            if dp[i][j] != 0:
                return dp[i][j]

            down_path = solve(i+1, j)
            up_path = solve(i, j+1) 

            dp[i][j] = down_path + up_path
            

            return dp[i][j]
        
        return solve(0,0)

        return dp[-1][-1]
        
