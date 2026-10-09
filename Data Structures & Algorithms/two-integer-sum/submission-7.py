class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash ={}
        for i,n in enumerate(nums):
            hash[n]= i 
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hash and hash[diff]!= i:
                return [i,hash[diff]]
        return [] 


           