class Solution:
    def minCostConnectPoints(self, points):
        if not points:
            return 0
        lengthInfo = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                length = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                lengthInfo.append((length, i, j))
        lengthInfo.sort(key=lambda x: x[0])
        mst = {0}
        ret = 0
        while len(mst) != len(points):
            n, length = None, float("inf")
            for l, i, j in lengthInfo:
                if l <= length and ((i in mst and j not in mst) or (i not in mst and j in mst)):
                    n, length = i, l
                    if i in mst:
                        n = j
                    break
            ret += length
            mst.add(n)
        return ret

if __name__ == "__main__":
    ret = Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])
    print(ret)
