class CQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def appendTail(self, value: int) -> None:
        self.in_stack.append(value)

    def deleteHead(self) -> int:
        if self.out_stack:
            return self.out_stack.pop()
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        if self.out_stack:
            return self.out_stack.pop()
        return -1
# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
