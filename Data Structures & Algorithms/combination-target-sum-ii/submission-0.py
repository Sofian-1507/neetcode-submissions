class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        subset=[]
        res=[]
        def dfs(i,target):
            if target==0:
                res.append(subset[:])
                return
            if i==len(nums) or target<0:
                return
            subset.append(nums[i])
            dfs(i+1,target-nums[i])
            subset.pop()
            while i+1<len(nums) and nums[i]== nums[i+1]:
                i+=1
            dfs(i+1,target)
        dfs(0,target)
        return res