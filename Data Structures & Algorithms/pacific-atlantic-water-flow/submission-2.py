class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        alt, pac =  set(), set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0),]

        def dfs(i,j,visited, prevH):
            if i < 0  or j < 0 or i >= rows or j >= cols or (i, j) in visited or heights[i][j] < prevH:
                return 
            visited.add((i,j))
            for (x,y) in directions:
                dfs(i+x,j+y,visited, heights[i][j])
             
        for i in range(rows):
            dfs(i,0,pac, heights[i][0])
            dfs(i,cols-1,alt, heights[i][cols-1] )
        
        for j in range(cols):
            dfs(0,j,pac, heights[0][j])
            dfs(rows-1,j,alt, heights[rows-1][j] )
        
        result = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in alt and (i, j) in pac:
                    result.append([i,j])

        return result