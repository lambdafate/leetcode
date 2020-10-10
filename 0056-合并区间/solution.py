class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        if not intervals:
            return ret
        intervals.sort(key=lambda x: (x[0], x[1]))
        intervals.append([float("inf"), float("inf")])
        begin, end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                ret.append([begin, end])
                begin, end = intervals[i][0], intervals[i][1]
        return ret