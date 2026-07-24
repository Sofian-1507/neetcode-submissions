class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False]*len(nums)
        subset = [] 
        res = [] 
        def dfs():
            if len(subset)==len(nums):
                res.append(subset[:])
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                subset.append(nums[i])
                used[i]=True
                dfs()
                subset.pop()
                used[i]=False
        dfs()
        return res
