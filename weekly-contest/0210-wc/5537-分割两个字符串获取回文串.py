class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if self.check(a) or self.check(b):
            return True
        return self.valid(a, b) or self.valid(b, a)

    def valid(self, a, b):
        i, j = 0, len(b)-1
        while i < j:
            if a[i] != b[j]:
                break
            i += 1
            j -= 1
        if i >= j:
            return True
        return self.check(b[i:j+1]) or self.check(a[i:j+1])

    def check(self, s):
        return len(s) == 0 or s == s[::-1]