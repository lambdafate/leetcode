class Solution:
    # 滑动窗口
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        l, r = 1, 2
        res = []
        while r < target:
            tmp = (l + r) * (r - l + 1) // 2
            if tmp == target:
                res.append(list(range(l, r+1)))
                l += 1
            elif tmp < target:
                r += 1
            else:
                l += 1
        return res
        
    """
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        for i in range(1, target-1):
            l, r = i, target - 1
            while l < r:
                mid = (l + r) // 2
                tmp = (mid + i) * (mid - i + 1) // 2
                if tmp == target:
                    res.append(list(range(i, mid+1)))
                    break
                elif tmp < target:
                    if l == mid:
                        break
                    l = mid
                else:
                    r = mid
        return res
    """
