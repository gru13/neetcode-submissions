class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def get_area(i, j):
            if i >= rows or i < 0:
                return 0
            if j >= cols or j < 0:
                return 0
            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            return 1 + get_area(i+1,j) + get_area(i-1,j) + get_area(i,j+1)+ get_area(i,j-1) 

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, get_area(i,j))
        return max_area

