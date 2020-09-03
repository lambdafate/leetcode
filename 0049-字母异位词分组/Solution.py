class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        cache = {}
        for s in strs:
            tmp = self.alive(s)
            if tmp in cache:
                cache[tmp].append(s)
            else:
                group = [s]
                ret.append(group)
                cache[tmp] = group
        return ret

    def alive(self, s):
        tmp = [c for c in s]
        tmp.sort()
        return "".join(tmp)
