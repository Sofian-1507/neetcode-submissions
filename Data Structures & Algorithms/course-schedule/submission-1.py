class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash = {i : [] for i in range(numCourses)}
        for c , p in prerequisites:
            hash[c].append(p)
        
        visit = set()

        def dfs(c):
            if c in visit : 
                return False
            if hash[c]==[]:
                return True
            visit.add(c)
            for p in hash[c]:
                if not dfs(p):
                    return False
            visit.remove(c)
            hash[c]=[]
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True