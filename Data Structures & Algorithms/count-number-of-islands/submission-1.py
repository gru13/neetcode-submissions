class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_island = 0
        rows,cols = len(grid), len(grid[0])
        def check_out_surrounding(i,j):
            nonlocal rows, cols

            if i >= rows or i < 0:
                return 
            if j >= cols or j < 0:
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            check_out_surrounding(i-1,j) #top       
            check_out_surrounding(i+1,j) #dwn       
            check_out_surrounding(i,j-1) #lft       
            check_out_surrounding(i,j+1) #ryt            


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    check_out_surrounding(i,j)
                    number_of_island += 1


        return number_of_island
                    