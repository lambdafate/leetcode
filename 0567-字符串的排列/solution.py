class Solution:

    # 暴力
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        index, end = 0, len(s2) - len(s1)
        s1 = list(s1)
        s1.sort()
        while index <= end:
            tmp = list(s2[index:index+len(s1)])
            tmp.sort()
            if tmp == s1:
                return True
            index += 1
        return False
        
