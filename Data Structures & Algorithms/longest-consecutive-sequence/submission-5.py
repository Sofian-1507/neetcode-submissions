class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        longest = 0
        for num in hash:
            if num-1 not in hash:
                count =1
                while num+count in hash:
                    count+=1
                longest = max(longest,count)
        return longest

            
        
