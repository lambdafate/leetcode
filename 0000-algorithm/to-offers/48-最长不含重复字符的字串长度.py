class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        norepeat = {}
        max_length, curr_length = 0, 0

        """
        for i, c in enumerate(s):
            if c in norepeat and norepeat[c] >= i - curr_length:
                curr_length = i - norepeat[c]
                norepeat[c] = i
                max_length = max(max_length, curr_length)
                continue
            norepeat[c] = i
            curr_length += 1
            max_length = max(max_length, curr_length)
        return max_length
        """
        for i, c in enumerate(s):
            if c in norepeat and norepeat[c] >= i - curr_length:
                curr_length = i - norepeat[c]
            else:
                curr_length += 1
            norepeat[c] = i
            max_length = max(max_length, curr_length)
        return max_length
