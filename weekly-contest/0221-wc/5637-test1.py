class Solution:
    def halvesAreAlike(self, s):
        i = len(s) // 2
        return self.Count(s[:i]) == self.Count(s[i:])

    def Count(self, s):
        cache = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count = 0
        for c in s:
            if c in cache:
                count += 1
        return count
