class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res= [0]*len(nums)
        st = [] 

        for i , t in enumerate(nums):
            while st  and  t> st[-1][0]:
                stackTemp,stackIndex=st.pop()
                res[stackIndex]=(i-stackIndex)
            st.append([t,i])
        return res