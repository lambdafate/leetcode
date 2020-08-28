class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ret = 0
        while x or y:
            ret += (x & 1) ^ (y & 1)
            x, y = x>>1, y>>1
        return ret