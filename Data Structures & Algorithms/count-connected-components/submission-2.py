class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i : [] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        count =0 
        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            for j in adj[i]:
                dfs(j)
        for c in range(n):
            if c not in visit:
                dfs(c)
                count+=1
        return count