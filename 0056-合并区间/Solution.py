class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) < 2:
            return intervals
        ret = []
        intervals.sort(key=lambda v:v[0])
        index = 0
        while index < len(intervals):
            i = index + 1
            end = intervals[index][1]
            while i < len(intervals) and intervals[i][0] <= end:
                i, end = i+1, max(end, intervals[i][1])
            
            ret.append([intervals[index][0], end])
            if i == len(intervals):
                break
            index = i
        return ret
