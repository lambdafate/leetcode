def readToInt():
    return [int(n) for n in input().split()]

def fuck(objects, target):
    i, j = 0, len(objects) - 1
    while i <= j:
        mid = i + (j - i) // 2
        if objects[mid] == target:
            return mid
        elif objects[mid] < target:
            i += 1
        else:
            j -= 1
    return -1

def solve(pictures):
    dp = [[1] * len(picture) for picture in pictures]
    max_length = 1
    for i in range(1, len(dp)):
        for j in range(len(pictures[i])):
            index = fuck(pictures[i-1], pictures[i][j])
            if index >= 0 and index < len(pictures[i-1]):
                # print(f"{pictures[i-1]} -- {pictures[i][j]} -- {index}")
                dp[i][j] = max(dp[i][j], 1 + dp[i-1][index])
                max_length = max(max_length, dp[i][j])
    return max_length

if __name__ == "__main__":
    for _ in range(int(input())):
        M = int(input())
        pictures = []
        for _ in range(M):
            line = readToInt()
            tmp = []
            for i in range(line[0]):
                tmp.append((line[1 + 2 * i], line[2 + 2 * i]))
            tmp.sort()
            pictures.append(tmp)
        print(solve(pictures))

