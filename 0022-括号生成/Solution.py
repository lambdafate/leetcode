class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.trace(n, n)

    def trace(self, left, right):
        if left == 0:
            return [")"*right]
        ret1 = self.trace(left-1, right)
        ret1 = ["(" + s for s in ret1]
        if left < right:    
            ret2 = self.trace(left, right-1)
            ret2 = [")" + s for s in ret2]
            ret1.extend(ret2)
        return ret1