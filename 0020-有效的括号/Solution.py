class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c== "{":
                stack.append(c)
                continue
            if not stack:
                return False
            pair = stack.pop()
            c, pair = pair, c
            if (c == "(" and pair != ")") or (c == "[" and pair != "]") or (c == "{" and pair != "}"):
                return False
        return len(stack) == 0