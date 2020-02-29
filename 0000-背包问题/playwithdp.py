# 动态规划解决01背包问题
bag_weight = 8

item_count = 4
item_weight = [0, 2, 3, 4, 5]
item_value  = [0, 3, 4, 5, 6]

def traceback(dp):
    row, clo = len(dp)-1, len(dp[0])-1
    res = []
    while dp[row][clo]:
        if dp[row][clo] == dp[row-1][clo]:
            row -= 1
            continue
        res.append(row)
        clo -= item_weight[row]
    return res

def main():
    dp = [[0] * (bag_weight+1) for _ in range(item_count+1)]
    for i in range(1, item_count+1):
        for j in range(1, bag_weight+1):
            if item_weight[i] > j:
                dp[i][j] = dp[i-1][j]
                continue
            # 检查是否要装入该物品
            if (fuck := item_value[i]+dp[i-1][j-item_weight[i]]) > dp[i-1][j]:
                dp[i][j] = fuck
            else:
                dp[i][j] = dp[i-1][j]
    print(" ", list(range(bag_weight+1)))
    for index, line in enumerate(dp):
        print(index, line)
    
    res = traceback(dp)
    
    wights = [item_weight[i] for i in res]
    values = [item_value[i]  for i in res]
    print("装入物品:\t", wights)
    print("物品价值:\t", values)

if __name__ == "__main__":
    main()