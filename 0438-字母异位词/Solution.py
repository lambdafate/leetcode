class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        if len(p) > len(s):
            return ret
        chars = {}
        for c in p:
            if c not in chars:
                chars[c] = 0
            chars[c] += 1
        i, j = 0, 0
        cache = {}
        while j < len(s):
            if s[j] not in chars:
                j += 1
                i = j
                cache.clear()
                continue
            cache[s[j]] = cache.get(s[j], 0) + 1
            if cache[s[j]] > chars[s[j]]:
                cache[s[j]] -= 1
                cache[s[i]] -= 1
                i += 1
                continue
            j += 1
            if (j-i) == len(p):
                ret.append(i)
                cache[s[i]] -= 1
                i += 1
        return ret