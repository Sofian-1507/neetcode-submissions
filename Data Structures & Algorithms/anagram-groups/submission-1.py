class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            check = ''.join(sorted(s))
            res[check].append(s)
        return list(res.values())
