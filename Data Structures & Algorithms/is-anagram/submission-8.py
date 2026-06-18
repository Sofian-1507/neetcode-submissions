class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        HashmapS={}
        HashmapT={}
        for i in range(len(s)):
            HashmapS[s[i]]=1+HashmapS.get(s[i],0)
            HashmapT[t[i]]=1+HashmapT.get(t[i],0)
        
        return HashmapS==HashmapT
            
            