class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        
        # Step 1: Initialize queue with all treasures
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        # Step 2: Multi-source BFS
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while queue:
            cur_x, cur_y = queue.popleft()
            for (x,y) in directions:
                next_x = x + cur_x
                next_y = y + cur_y 
                if next_x < 0 or next_x >= rows or next_y < 0 or next_y >= cols:
                    continue
                if grid[next_x][next_y] == -1:
                    continue
                if grid[next_x][next_y] == 2147483647:
                    queue.append((next_x, next_y))
                    grid[next_x][next_y] =  grid[cur_x][cur_y]+1