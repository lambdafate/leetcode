class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n < 0:
            return []
        if n == 0:
            return [0]
        bits = ['0'] * n
        cache = {'0' * n}
        ret = [0]
        while len(ret) < 2**n:
            for i in range(n):
                bit = bits[i]
                bits[i] = '1' if bit == '0' else '0'
                tmp = "".join(bits)
                if tmp not in cache:
                    cache.add(tmp)
                    ret.append(self.convertInt(tmp))
                    break
                bits[i] = bit
        return ret

    def convertInt(self, s):
        ret = 0
        mask = 1
        for i in range(len(s)-1, -1, -1):
            ret += int(s[i]) * mask
            mask = mask << 1
        return ret