class Solution:
    def __init__(self):
        self.cache = {}

    """
        不用cache直接超出时间限制, 使用cache直接beat 96.38%
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        wordSet = set()
        minLength, maxLength = float("inf"), 0
        for word in wordDict:
            wordSet.add(word)
            minLength = min(minLength, len(word))
            maxLength = max(maxLength, len(word))
        ret = self.trace(s, 0, minLength, maxLength, wordSet)
        return ret

    def trace(self, s, index, minLength, maxLength, wordSet):
        if index >= len(s):
            return True
        if index in self.cache:
            return self.cache[index]
        ret = False
        for length in range(minLength, maxLength+1):
            if s[index:index+length] in wordSet and self.trace(s, index+length, minLength, maxLength, wordSet):
                ret = True
                break
        self.cache[index] = ret
        return ret
        