class Solution:
    def countBits(self, num: int) -> List[int]:
        ret = [0] * (num+1)
        for n in range(1, num+1):
            if n % 2 == 0:
                ret[n] = ret[n//2]
            else:
                ret[n] = ret[n-1] + 1
        return ret

    """
    def countBits(self, num: int) -> List[int]:
        ret = []
        for n in range(num+1):
            tmp = 0
            while n:
                tmp += n & 1
                n = n >> 1
            ret.append(tmp)
        return ret
    """