def solve(pattern, target):
    i, j = 0, 0
    while i < len(pattern) and j < len(target):
        if pattern[i] == "*":
            tmp = pattern[i+1:]
            k = j
            while k <= len(target) and not solve(tmp, target[k:]): k += 1
            return k <= len(target)
        if pattern[i] == "?" or pattern[i] == target[j]:
            i += 1
            j += 1
        else:
            return False
    if j < len(target):
        return False
    while i < len(pattern):
        if pattern[i] != "*":
            return False
        i += 1
    return True

pattern = input()
target = input()
if solve(pattern, target):
    print(1)
else:
    print(0)
