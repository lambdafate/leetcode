class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        self.backtrace(candidates, 0, [], ret, target)
        return ret
    
    def backtrace(self, candidates, index, path, ret, target):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        tmp = -1
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            if candidates[i] == tmp:
                continue
            tmp = candidates[i]
            self.backtrace(candidates, i + 1, path + [candidates[i]], ret, target-candidates[i])
        