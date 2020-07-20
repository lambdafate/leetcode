class Solution:
    def fib(self, n: int) -> int:
        i, j = 0, 1
        while n != 0:
            i, j = j, i+j
            i %= 1000000007
            n -= 1
        return i
