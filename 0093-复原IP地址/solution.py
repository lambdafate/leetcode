class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []
        self.dfs(s, [], ret)
        return ret

    def dfs(self, s, path, ret):
        if len(path) > 4 or (len(path) < 4 and not s):
            return None
        if len(path) == 4 and not s:
            ret.append(".".join(path))
            return None
        if s[0] == '0':
            self.dfs(s[1:], path+[s[0]], ret)
            return None
        v = 0
        for i, c in enumerate(s):
            v = v * 10 + int(c)
            if v > 255:
                break
            self.dfs(s[i+1:], path+[s[:i+1]], ret)
        return None