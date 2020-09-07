class Solution:
    def decodeString(self, s: str) -> str:
        ret = self.dfs(s, 0, len(s)-1)
        return ret

    def dfs(self, s, i, j):
        if i > j:
            return ""
        ret = ""
        while i <= j and not s[i].isdigit():
            ret += s[i]
            i += 1
        if i > j:
            return ret
        num = ""
        while s[i].isdigit():
            num += s[i]
            i += 1
        begin, end = i+1, i+1
        tmp = 1
        while end <= j and tmp != 0: 
            if s[end] == '[':
                tmp += 1
            elif s[end] == ']':
                tmp -= 1
            end += 1
        decodestr = self.dfs(s, begin, end-2)
        ret = ret + decodestr * int(num) + self.dfs(s, end, j)
        return ret      
