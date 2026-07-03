class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()
        def dfs(i,j,k):
            if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited or word[k] != board[i][j]:
                return False
            if k == len(word)-1:
                return True

            visited.add((i,j))

            for (x,y) in [(0,1), (1,0), (0,-1), (-1,0)]:
                if dfs(x+i, y+j, k+1):
                    return True

            visited.remove((i,j))
            return False


        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    if dfs(i,j,0):
                        return True
        return False