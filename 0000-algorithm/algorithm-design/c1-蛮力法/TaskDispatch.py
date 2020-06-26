"""
    任务分配问题
"""

import sys


def task_dispatch(costs):
    tasks_number = len(costs)
    tasks = [0] * tasks_number
    min_cost = sys.maxsize

    def helper(person, cost):
        if person == tasks_number-1:
            nonlocal min_cost
            min_cost = min(min_cost, cost + costs[person][tasks.index(0)])
            return None
        for i in range(tasks_number):
            if tasks[i] == 1:
                continue
            tasks[i] = 1
            helper(person+1, cost+costs[person][i])
            tasks[i] = 0
    helper(0, 0)
    return min_cost


if __name__ == "__main__":
    costs = [
        [9, 2, 7],
        [6, 4, 3],
        [5, 8, 1]
    ]
    print(f"costs => {costs}")

    print(f"min cost => {task_dispatch(costs)}")