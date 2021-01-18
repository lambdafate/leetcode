input()
nums = list(map(int, input().split()))
input()
requests = list(map(int, input().split()))

desc_order = {}
asc_order = {}

def mergeSort(nums, order):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid], order)
    right = mergeSort(nums[mid:], order)
    ret = []
    i, j = 0, 0
    right_num = 0
    count = 0
    while i < len(left) or j < len(right):
        if i >= len(left):
            ret.append(right[j])
            j += 1
            right_num += 1
        elif j >= len(right):
            ret.append(left[i])
            i += 1
            count += right_num
        else:
            if left[i] <= right[j]:
                ret.append(left[i])
                i += 1
                count += right_num
            else:
                ret.append(right[j])
                j += 1
                right_num += 1
    order[len(ret)] = order.get(len(ret), 0) + count
    return ret

def solve(nums, requests):
    ans = []
    # init
    mergeSort(nums, desc_order)
    mergeSort(nums[::-1], asc_order)
    for q in requests:
        length = 2**q
        while length >= 2:
            desc_order[length], asc_order[length] = asc_order[length], desc_order[length]
            length = length // 2
        ans.append(sum(desc_order.values()))
    return ans


ans = solve(nums, requests)
for n in ans:
    print(n)

