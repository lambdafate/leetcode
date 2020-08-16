class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        helper = []
        while pushed:
            helper.append(pushed.pop(0))
            while helper and helper[-1] == popped[0]:
                helper.pop()
                popped.pop(0)
        if not helper or helper[::-1] == popped:
            return True
        return False