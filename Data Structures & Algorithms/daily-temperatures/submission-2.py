class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        st = [] 
        for i,t in enumerate(nums):
            while st and t>st[-1][0]:
                stt,sti=st.pop()
                res[sti]=i-sti
            st.append([t,i])
        return res