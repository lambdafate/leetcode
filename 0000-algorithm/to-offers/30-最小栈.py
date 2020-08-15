class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.helper.append(x if len(self.helper)==0 else min(self.helper[-1], x))

    def pop(self) -> None:
        self.stack.pop()
        self.helper.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.helper[-1]