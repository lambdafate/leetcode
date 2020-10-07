class SortedStack:

    def __init__(self):
        self.stack = []
        self.helper = []

    def push(self, val: int) -> None:
        while self.stack and self.stack[-1] < val:
            self.helper.append(self.stack.pop())
        self.stack.append(val)
        while self.helper:
            self.stack.append(self.helper.pop())
        return None 

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def peek(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.stack) == 0

# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
