class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r,c):
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!=1 or (r,c) in visit):
                return 
            q.append((r,c))
            grid[r][c]=2
            visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                    visit.add((r,c))
        count = 0 
        
        while q : 
            for i in range(len(q)):
                r,c =q.popleft()
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            count+=1

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1
        return max(0,count-1)
            

