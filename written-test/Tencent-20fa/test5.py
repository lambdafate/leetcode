line = input().split()
n, L = int(line[0]), int(line[1])
dogs = []
for _ in range(n):
    tmp = [int(n) for n in input().split()]
    dogs.append(tmp)
dogs.sort(key=lambda x: (x[0], -x[1]))
prev_left, prev_right = float("-inf"), 0
count = 0
i = 0
while i < len(dogs):
    if L <= prev_right: break
    j = i
    next_dog = None 
    length = 0
    while j < len(dogs) and dogs[j][0] <= prev_right:
        tmp = dogs[j][1] - prev_right
        if tmp > length:
            next_dog = j
            length = tmp
        j += 1
    if next_dog == None:
        break
    count += 1
    prev_left, prev_right = dogs[next_dog][0], dogs[next_dog][1]
    i = next_dog + 1

if L <= prev_right:
    print(count)
else:
    print(-1)