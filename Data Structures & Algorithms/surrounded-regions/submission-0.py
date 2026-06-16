from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        rows, cols = len(board), len(board[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(rows):
            if board[i][0] == "O":
                queue.append((i,0))
                board[i][0] = "T"
            if board[i][cols-1] == "O":
                queue.append((i,cols-1))
                board[i][cols-1] = "T"

        for j in range(cols):
            if board[0][j] == "O":
                queue.append((0,j))
                board[0][j] = "T"

            if board[rows-1][j] == "O":
                queue.append((rows-1, j))
                board[rows-1][j] = "T"

    
        print(queue)
        while len(queue):
            i,j = queue.popleft()
            for (x,y) in directions:
                nx, ny = i+x, j+y 
                if nx < 0 or ny < 0 or nx >= rows or ny >= cols or board[nx][ny] != "O":
                    continue
                board[nx][ny] = "T"
                queue.append((nx,ny))
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O" 
