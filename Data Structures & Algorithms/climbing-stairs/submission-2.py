class Solution:
    def climbStairs(self, n: int) -> int:
        
        x=1
        y=1
        for i in range(2,n+1):
            z=x+y
            y=x
            x=z
        return x 
        
