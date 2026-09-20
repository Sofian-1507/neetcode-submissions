class Solution:
    def searchMatrix(self, grid: List[List[int]], target: int) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            l=0
            r=cols-1
            while l<=r:
                mid = l+(r-l)//2
                if grid[row][mid]==target:
                    return True
                elif grid[row][mid]<target:
                    l=mid+1
                else:
                    r=mid-1
        return False


