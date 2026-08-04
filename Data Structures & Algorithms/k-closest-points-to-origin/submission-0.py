class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        heapq.heapify(heap)
        for x,y in points :
            dist = x*x+y*y
            heapq.heappush(heap,(dist,(x,y)))
        
        while k != 0 :
            dist , point =heapq.heappop(heap)
            res.append(point)
            k-=1
        return res

        
