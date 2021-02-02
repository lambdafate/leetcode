def solve(num):
    while num > 0:
        tmp = 0
        while num != 0:
            tmp += (num % 10)**2
            num = num // 10
        if tmp == 1: return True
        num = tmp
    return False

for _ in range(int(input())):
    num = int(input())
    if solve(num):
        print("true")
    else:
        print("false")