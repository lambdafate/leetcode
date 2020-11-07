class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        cache = {point[0] for point in points}
        X = list(cache)
        X.sort()
        ret = 0
        for i in range(1, len(X)):
            ret = max(ret, X[i] - X[i-1])
        return ret
