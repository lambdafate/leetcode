class Solution:
    def lengthOfLastWord(self, s):
        res = s.strip().split(" ")
        return len(res[-1]) if res else 0