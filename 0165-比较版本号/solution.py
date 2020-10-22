class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        i, j = 0, 0
        while i < len(version1) and j < len(version2):
            num1, num2 = int(version1[i]), int(version2[j])
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            else:
                i, j = i+1, j+1
        if i >= len(version1) and j >= len(version2):
            return 0
        ret = 1
        check = version1[i:]
        if i >= len(version1):
            ret = -1
            check = version2[j:]
        for num in check:
            if int(num) > 0:
                return ret
        return 0