class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        count = 0
        points.sort(key=lambda x: x[0])
        begin, end = points[0][0], points[0][1]
        i = 0
        while i < len(points):
            point = points[i]
            if point[0] <= end:
                begin = max(begin, point[0])
                end = min(end, point[1])
            else:
                count += 1
                begin, end = point[0], point[1]
            i += 1
        count += 1
        return count
