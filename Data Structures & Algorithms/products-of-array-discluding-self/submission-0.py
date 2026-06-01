class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [] 
        for i in range(len(nums)):
            k=1
            for j in range(len(nums)):
                if i!=j:
                    k*=nums[j]
                
            res.append(k)

        return res


        