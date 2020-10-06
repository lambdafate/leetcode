from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""
        cache = Counter(s)
        ret = []
        for c in s:
            cache[c] -= 1
            if c in ret:
                continue
            while ret and ret[-1] > c and cache[ret[-1]] > 0:
                ret.pop()
            ret.append(c)
        return "".join(ret)
