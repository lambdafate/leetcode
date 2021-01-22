# special case: 
#     s = "a"
#     p = "a*a"
# 从while循环中break后，
#     如果p[j] != "*", 那么直接验证p[j:]是否匹配空串
#     否则, 既可以拿p[j-1]匹配s[i-1], p[j+1:]匹配空串, 
#     也可以拿p[j-1:j+1]匹配空串, p[j+1:]匹配s[i-1:]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(p):
            if p[j] == ".":
                j += 1
                i += 1
                continue
            if p[j] == "*":
                if self.isMatch(s[i-1:], p[j+1:]): return True
                k = i - 1
                while k < len(s) and (p[j-1] == "." or p[j-1] == s[k]):
                    if self.isMatch(s[k+1:], p[j+1:]): return True
                    k += 1
                return False
            if s[i] == p[j]:
                i += 1
                j += 1
            elif j + 1 < len(p) and p[j + 1] == "*":
                j += 2
            else:
                return False
        if i < len(s):
            return False
        if j < len(p) and p[j] == "*":
            j += 1
            if self.isMatch(s[i-1:], p[j:]):
                return True
        while j < len(p):
            if p[j] != "*" and (j + 1 >= len(p) or p[j + 1] != "*"):
                return False
            j += 1
        return True

if __name__ == "__main__":
    s = "a"
    p = "a*a"
    match = Solution()
    ans = match.isMatch(s, p)
    print(ans)