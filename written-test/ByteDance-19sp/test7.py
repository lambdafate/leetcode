def readToInt():
    return [int(n) for n in input().split()]

def fuck(H, power):
    for i in range(len(H)):
        if power < 0: return False
        if H[i] > power:
            power -= H[i] - power
        else:
            power += power - H[i]
    return power >= 0

def solve(H):
    i, j = 0, sum(H)
    while i < j:
        mid = i + (j - i) // 2
        if fuck(H, mid):
            j = mid
        else:
            i = mid + 1
    return i

if __name__ == "__main__":
    input()
    H = readToInt()
    print(solve(H))
