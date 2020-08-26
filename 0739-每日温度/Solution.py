class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        signle_stack = []
        result = [0] * len(T)
        for index, value in enumerate(T):
            while signle_stack and T[signle_stack[-1]] < value:
                result[signle_stack[-1]] = index - signle_stack[-1]
                signle_stack.pop()
            signle_stack.append(index)
        return result