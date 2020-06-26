"""
    0/1背包问题
"""


# 0/1背包问题, 选择最大价值
def select_max_value(weights, values, bag):
    # 从下标为begin的物品开始, 总重量不超过bag的最大价值
    def helper(begin, bag):
        value = 0
        if begin >= len(values):
            pass
        elif weights[begin] > bag:
            value = helper(begin+1, bag)
        else:
            value = max(values[begin]+helper(begin+1, bag-weights[begin]),
                        helper(begin+1, bag))
        return value

    return helper(0, bag)


if __name__ == "__main__":
    weights = [7, 3, 4, 5]
    values = [42, 12, 40, 25]
    bag = 10
    print(f"weights: {weights}")
    print(f"values : {values}")
    print(f"bag    : {bag}")

    print(f"max value => {select_max_value(weights, values, bag)}")