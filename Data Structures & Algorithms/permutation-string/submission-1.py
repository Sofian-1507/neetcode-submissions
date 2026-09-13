class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        
        count1 = {}
        count2 = {}

        for ch in s1:
            count1[ch] = count1.get(ch, 0) + 1
        
        i = 0 
        j = len(s1)-1
        for ch in s2[i:j+1]:
            count2[ch]=count2.get(ch,0)+1

        if count1 == count2:
            return True

        while j < len(s2)-1:
            count2[s2[i]]-=1
            if count2[s2[i]]==0:
                del count2[s2[i]]
            i+=1

            j+=1
            count2[s2[j]] = count2.get(s2[j], 0) + 1
            if count1 == count2:
                return True

        return False