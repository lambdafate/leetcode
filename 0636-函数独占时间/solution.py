class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if n < 1 or not logs:
            return []
        for i in range(len(logs)):
            tmp = logs[i].split(":")
            logs[i] = (int(tmp[0]), tmp[1], int(tmp[2]))
        ret = [0] * n
        stack = [logs[0]]
        last = logs[0]
        for i in range(1, len(logs)):
            if logs[i][1] == "start":
                if stack:
                    ret[stack[-1][0]] += logs[i][2] - last[2] + (-1 if last[1] == 'end' else 0)
                stack.append(logs[i])
            else:
                ret[stack[-1][0]] += logs[i][2] - last[2] + (0 if last[1] == 'end' else 1)
                stack.pop()
            last = logs[i]
        return ret