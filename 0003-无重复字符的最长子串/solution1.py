class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = 0
        helper = {}
        ret = 0
        while index < len(s):
            if s[index] not in helper:
                helper[s[index]] = index
                index += 1
                ret = max(ret, len(helper))
                continue
            i = helper[s[index]]
            helper = {k:v for k, v in helper.items() if v > i}
            helper[s[index]] = index
            index += 1
            ret = max(ret, len(helper))
        return ret    

    def lengthOfLongestSubstring(self, s: str) -> int:
        index = 0
        helper = {}
        ret, maxLength = 0, 0
        while index < len(s):
            if s[index] not in helper or helper[s[index]] + maxLength < index:
                helper[s[index]] = index
                index += 1
                maxLength += 1
                ret = max(ret, maxLength)
                continue
            maxLength = index - helper[s[index]]
            helper[s[index]] = index
            ret = max(ret, maxLength)
            index += 1
        return ret
