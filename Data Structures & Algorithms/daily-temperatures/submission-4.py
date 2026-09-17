class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [0]
        for i in range(1,len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev=stack.pop()
                res[prev]=i-prev
            
            stack.append(i)
        return res