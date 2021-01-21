def readToInt():
    return [int(n) for n in input().split()]

positions = readToInt()
i = 0
length = float("-inf")
while i < len(positions):
    if positions[i] == 1:
        i += 1
        continue
    j = i
    while j < len(positions) and positions[j] == 0: j += 1
    tmp = j - i
    if j >= len(positions) or i == 0:
        length = max(length, tmp)
    else:
        length = max(length, (tmp + 1) // 2) 
    i = j
print(length)
