from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minute = 0
        fresh_fruits = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_fruits += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        print(queue)
        while len(queue):
            len_queue = len(queue)
            for _ in range(len_queue):
                i, j = queue.popleft()
                for (x,y) in directions:
                    nx, ny = i+x, j+y
                    if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                        continue
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_fruits -= 1
                        queue.append((nx, ny))

            minute += 1
        
        if fresh_fruits:
            return -1
        
        return max(minute - 1, 0)