class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        helper = {}
        length = 0
        for i, c in enumerate(s):
            if c not in helper or helper[c] + length < i:
                helper[c] = i
                length += 1
            else:
                length = i - helper[c]
                helper[c] = i
            ret = max(ret, length)
        return ret


    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        helper = {}
        for i, c in enumerate(s):
            if c not in helper:
                helper[c] = i
            else:
                index = helper[c]
                helper = { k:v for k, v in helper.items() if v > index}
                helper[c] = i
            ret = max(ret, len(helper))
        return ret




    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        for i in range(len(s)):
            helper = set()
            for j in range(i, len(s)):
                if s[j] in helper:
                    break
                helper.add(s[j])
                ret = max(ret, len(helper))

        return ret
