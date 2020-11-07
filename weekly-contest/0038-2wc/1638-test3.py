class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ret = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                tmp = s[i:j+1]
                for index in range(len(t) - len(tmp) + 1):
                    if self.check(tmp, t[index:index+len(tmp)]):
                        ret += 1
        return ret

    def check(self, s1, s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        return count == 1
