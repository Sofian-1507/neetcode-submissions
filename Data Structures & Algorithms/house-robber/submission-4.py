class Solution:
    def rob(self, nums: List[int]) -> int:
        x,y = 0 ,0 
        for num in nums :
            temp = max(num+x,y)
            x=y
            y=temp
        return y