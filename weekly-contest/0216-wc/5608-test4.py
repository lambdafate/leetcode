class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1])
        allEffort = 0
        leftEffort = 0
        i = 0
        while i < len(tasks):
            if leftEffort < tasks[i][1]:
                allEffort += tasks[i][1] - leftEffort
                leftEffort = tasks[i][1]
            else:
                leftEffort -= tasks[i][0]
                i += 1
        return allEffort


    """
    # 超时
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        left, right = float("inf"), 0
        for task in tasks:
            left = min(left, task[1])
            right += task[1]
        while left < right:
            mid = (left + right) // 2
            ret = self.dfs(tasks, mid)
            if ret:
                right = mid
            else:
                left = mid + 1
        return left

    def dfs(self, tasks, allEffort):
        if not tasks:
            return True
        for i, task in enumerate(tasks):
            if allEffort >= task[1]:
                tasks.remove(task)
                if self.dfs(tasks, allEffort - task[0]):
                    tasks.insert(i, task)
                    return True
                tasks.insert(i, task)
        return False
                
    """            
