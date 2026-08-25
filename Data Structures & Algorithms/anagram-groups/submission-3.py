class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        for s in strs:
            key = "".join(sorted(s))
            if key not in hash:
                hash[key]=[]
            hash[key].append(s)
        
        res = [] 
        for key in hash : 
            res.append(hash[key])
        return res