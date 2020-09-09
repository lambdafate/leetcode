class Solution:
    def __init__(self):
        self.cache = {0: [[]]}

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        self.dfs(candidates, 0, [], ret, target)
        return ret

    def dfs(self, candidates, index, path, ret, target):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
        for i in range(index, len(candidates)):
            if target < candidates[i]:
                break
            self.dfs(candidates, i, path+[candidates[i]], ret, target-candidates[i])

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = self.trace(candidates, target)
        result = []
        for path in ret:
            path.sort()
            if path not in result:
                result.append(path)
        return result

    def trace(self, candidates, target):
        ret = []
        if target in self.cache:
            return [v[:] for v in self.cache[target]]
        for num in candidates:
            if target < num:
                break
            tmp = self.combinationSum(candidates, target-num)
            for i in range(len(tmp)):
                tmp[i].append(num)
            ret.extend(tmp)
        self.cache[target] = [v[:] for v in ret]
        return ret

