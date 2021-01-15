def readToInt():
    return [int(n) for n in input().split()]

def solve(queue, m):
    ret = []
    i = 0
    while i < len(queue):
        tmp = queue[i:i+m][::-1]
        ret += tmp
        i += m
    return ret[::-1]


if __name__ == "__main__":
    line = readToInt()
    queue = readToInt()
    for q in solve(queue, line[1]):
        print(q, end=" ")