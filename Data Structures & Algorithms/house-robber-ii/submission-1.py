class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def dfs(arr):
            y,x=0,0
            for i in arr:
                curr= max(x,y+i)
                y=x
                x=curr
            return x
        
        return max(
            dfs(nums[:-1]),
            dfs(nums[1:])

        )
        