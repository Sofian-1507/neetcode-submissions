class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hash = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            hash[crs].append(pre)
        
        visited = set()
        visiting = set()
        res = [] 
        def dfs(crs):
            if crs in visiting :
                 return False
            if crs in visited:
                return True
            if hash[crs]==[]:
                visited.add(crs)
                res.append(crs)
                return True
            visiting.add(crs)
            for pre in hash[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            visited.add(crs)
            hash[crs] = []
            res.append(crs)
            return True

            
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res