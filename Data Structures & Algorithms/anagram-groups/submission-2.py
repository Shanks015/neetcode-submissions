class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for i in strs:
            s = tuple(sorted(i))
            if s not in di:
                di[s] = [i]
            else:
                di[s].append(i)
        return list(di.values())