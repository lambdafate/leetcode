class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        while n != 0:
            num += 1
            n &= (n-1)
        return num

    """
    def hammingWeight(self, n: int) -> int:
        num = 0
        while n != 0:
            tmp = n % 2
            n = n // 2
            if tmp != 0:
                num += 1
        return num
    """