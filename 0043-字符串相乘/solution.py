from collections import deque

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = self.strToInt(num1)
        num2 = self.strToInt(num2)
        queue = deque()
        num = num1 * num2
        if num == 0:
            return "0"
        while num:
            tmp = num % 10
            num = num // 10
            queue.appendleft(chr(ord('0') + tmp))
        return "".join(list(queue))

    def strToInt(self, s):
        ret = 0
        for c in s:
            ret = ret * 10 + ord(c) - ord('0')
        return ret