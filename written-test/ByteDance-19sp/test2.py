def readToInt():
    return [int(n) for n in input().split()]

def fuck(nums, index, target):
    i, j = index, len(nums) - 1
    while i < j:
        mid = i + (j - i) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            if i == mid:
                if nums[j] <= target:
                    return j
                return i
            i = mid
        else:
            j = mid - 1
    return i

def solve(positions, D):
    count = 0
    for i in range(len(positions) - 2):
        j = fuck(positions, i, positions[i] + D)
        if i + 2 <= j:
            n = j - i
            count += (n - 1) * n // 2
    return count % 99997867



if __name__ == "__main__":
    line = readToInt()
    positions = readToInt()
    if line[0] < 3 or line[1] <= 0:
        print(0)
    else:
        print(solve(positions, line[1]))
        
