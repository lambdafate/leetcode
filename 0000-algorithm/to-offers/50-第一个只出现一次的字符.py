class Solution:
    def firstUniqChar(self, s: str) -> str:
        helper = {}
        for c in s:
            if c not in helper:
                helper[c] = 0
            helper[c] += 1
        for c in s:
            if helper[c] == 1:
                return c
        return " "
