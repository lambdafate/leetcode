class Solution:
    # 桶思想
    def leastInterval(self, tasks, n):
        if n <= 0:
            return len(tasks)
        helper = {}
        height = 0
        for task in tasks:
            if task not in helper:
                helper[task] = 0
            helper[task] += 1
            height = max(helper[task], height)
        maxCount = 0
        for v in helper.values():
            if v == height:
                maxCount += 1
        return max((height - 1) * (n + 1) + maxCount, len(tasks))


    """
    # error
    def leastInterval(self, tasks, n):
        if n <= 0:
            return len(tasks)
        ticks, index = 0, 0
        cold = {}
        while tasks:
            if tasks[index] not in cold or ticks - cold[tasks[index]] >= n:
                ticks += 1
                cold[tasks[index]] = ticks
                tasks.pop(index)
                index = 0 if index == len(tasks) else index
                continue

            tmp = (index + 1) % len(tasks)
            while tasks[tmp] in cold and ticks - cold[tasks[tmp]] < n and tmp != index:
                tmp = (tmp + 1) % len(tasks)
            if tmp == index:
                ticks += 1
            else:
                index = tmp
        return ticks
    """            


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    Solution().leastInterval(tasks, n)
