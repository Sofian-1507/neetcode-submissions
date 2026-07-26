class Solution:
    def partition(self, s: str) -> List[List[str]]:
        subset = [] 
        res = [] 
        def dfs(i):
            if i == len(s):
                res.append(subset[:])
                return 
            for end in range(i,len(s)):
                curr = s[i:end+1]
                if curr == curr[::-1]:
                    subset.append(curr)
                    dfs(end+1)
                    subset.pop()
        
        dfs(0)
        return res