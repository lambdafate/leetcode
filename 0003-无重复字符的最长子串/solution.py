class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        helper = {}
        curr_length = 0
        res = 0
        for i, c in enumerate(s):
            if c in helper and helper[c] >= i-curr_length:
                curr_length = i - helper[c]
                helper[c] = i
            else:
                helper[c] = i
                curr_length += 1
            res = max(res, curr_length)
        return res 
