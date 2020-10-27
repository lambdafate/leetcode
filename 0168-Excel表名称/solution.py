from collections import deque

class Solution:
    def convertToTitle(self, n: int) -> str:
        queue = deque()
        while n != 0:
            num = n % 10
            n = n // 10
            queue.appendleft(self.getCahrfromNum(num))
        return "".join(list(queue))        

    def getCahrfromNum(self, num):
        return chr(ord('A') + num - 1)