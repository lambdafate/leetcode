class CQueue:
    def __init__(self):
        self.first = []
        self.second = []

    def appendTail(self, value: int) -> None:
        self.first.append(value)

    def deleteHead(self) -> int:
        if self.second:
            return self.second.pop()
        while self.first:
            self.second.append(self.first.pop())
        if self.second:
            return self.second.pop()
        return -1




# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
