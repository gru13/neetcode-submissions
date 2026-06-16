from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0),(0, -1)]
        minute = 0
        queue = deque()
        num_fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    num_fresh += 1


        while len(queue):
            len_q = len(queue)
            minute += 1
            for _ in range(len_q):
                cur_x, cur_y = queue.popleft()
                for (x,y) in directions:
                    nx = cur_x + x
                    ny = cur_y + y
                    if  nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                        continue 
                    if grid[nx][ny] == 1:
                        num_fresh -= 1
                        grid[nx][ny] = 2
                        queue.append((nx,ny))
        
        if num_fresh:
            return -1
        return max(minute - 1, 0);