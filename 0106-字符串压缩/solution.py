class Solution:
    def compressString(self, S: str) -> str:
        ret = []
        i = 0
        while i < len(S):
            j = i
            while j < len(S) and S[i] == S[j]:
                j += 1
            ret.append(S[i] + str(j-i))
            i = j
        res = "".join(ret)
        if len(S) <= len(res):
            return S
        return res