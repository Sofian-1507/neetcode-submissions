class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        x,y=0,0
        for i in cost :
            curr = min(x,y)+i
            x,y=y,curr
        return min(x,y)