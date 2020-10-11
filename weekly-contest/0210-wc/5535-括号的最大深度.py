class Solution:
    def maxDepth(self, s: str) -> int:
        if not s:
            return 0
        ret = 0
        left = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                left -= 1
            ret = max(left, ret)
        return ret