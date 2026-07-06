class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hash = {i:[]for i in range(numCourses)}
        for c,p in prerequisites:
            hash[c].append(p)
        
        res = []
        visit,cycle=set(),set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in hash[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        

        for c in range(numCourses):
            if dfs(c)==False:
                return []
        return res
            