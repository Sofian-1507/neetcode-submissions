class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix),len(matrix[0])
        for row in range(rows):
            l= 0 
            r=cols -1 

            while l <= r :
                m = l + ((r-l)//2)
                if target > matrix[row][m]:
                     l = m+1
                elif target < matrix[row][m]:
                    r = m-1
                else :
                    return True
        return False