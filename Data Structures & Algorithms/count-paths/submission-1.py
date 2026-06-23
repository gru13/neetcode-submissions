class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        def solve(i,j, visited):
            if (i == m - 1 and j == n - 1):
                return 1

            if i >= m or j >= n or (i, j) in visited:
                return 0

            if dp[i][j] != 0:
                return dp[i][j]
            visited.add((i,j))

            down_path = solve(i+1, j, visited)
            up_path = solve(i, j+1, visited) 

            dp[i][j] = down_path + up_path
            
            visited.remove((i,j))

            return dp[i][j]
        
        return solve(0,0, set())

        return dp[-1][-1]
        
