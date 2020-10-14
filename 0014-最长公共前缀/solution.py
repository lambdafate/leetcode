class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        if not strs:
            return ret
        i = 0
        while True:
            if i >= len(strs[0]):
                break
            c = strs[0][i]
            flag = False
            for s in strs:
                if i >= len(s) or s[i] != c:
                    flag = True
                    break
            if flag:
                break
            ret += c
            i += 1
        return ret
            