class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if n <= 0 or k <= 0:
            return ""
        ret = ['a'] * n
        allSum, i = n, n - 1
        while i >= 0 and allSum != k:
            tmp = allSum - self.getValue(ret[i])
            left = k - tmp
            if left >= 1 and left <= 26:
                ret[i] = self.getChar(left)
                allSum = k
            else:
                ret[i] = 'z'
                allSum = tmp + 26
                i -= 1
        return "".join(ret)

    
    def getChar(self, num):
        return chr(ord('a') + num - 1)
    
    def getValue(self, char):
        return ord(char) - ord('a') + 1