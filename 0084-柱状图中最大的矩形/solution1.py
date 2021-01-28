class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = heights
        area = 0
        # init
        bad = [False] * len(h)
        i = 0
        while i < len(h):
            if not bad[i]:
                area = max(area, h[i])
                j, height = i + 1, h[i]
                while j < len(h) and not bad[j]:
                    if h[j] <= height:
                        height = h[j]
                        bad[j] = True
                    area = max(area, height * (j - i + 1))
                    j += 1
            i += 1
        return area
