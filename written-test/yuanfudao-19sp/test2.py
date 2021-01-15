def solve(s, length):
    part_length = (length - 1) // 3
    width = part_length * 2 + 1
    index = 0
    for i in range(part_length):
        print(f"{' ' * i}{s[index]}{' ' * (width - 2 * i - 2)}{s[index+1]}")
        index += 2
    for _ in range(part_length + 1):
        print(f"{' ' * part_length}{s[index]}")
        index += 1
    return
    

if __name__ == "__main__":
    length = int(input())
    s = input()
    solve(s, length)