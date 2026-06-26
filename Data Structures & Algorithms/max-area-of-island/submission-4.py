class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows , cols = len(grid),len(grid[0])
        maxi = 0 

        def dfs(r,c):
            if (r<0 or c<0 or r>=rows or c >= cols or grid[r][c]==0):
                return 0
            grid[r][c]=0
            count =1 
            for dr,dc in directions :
                count+=dfs(r+dr,c+dc)
            return count 


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area = dfs(r,c)
                    maxi = max(maxi,area)
        return maxi
