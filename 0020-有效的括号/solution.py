class Solution:
    # '('，')'，'{'，'}'，'['，']'
    def __init__(self):
        self.lefts = list("([{")
        self.rights = list(")]}")

    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for c in s:
            if c in self.lefts:
                stack.append(c)
                continue
            if stack and self.lefts[self.rights.index(c)] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
