class Solution:
    def __init__(self):
        self.helper = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                       '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        if len(digits) == 0:
            return ret
        self.trace(digits, 0, "", ret)
        return ret

    def trace(self, digits, index, prev_str, ret):
        if index >= len(digits):
            ret.append(prev_str)
            return
        for c in self.helper[digits[index]]:
            self.trace(digits, index+1, prev_str+c, ret)
        
