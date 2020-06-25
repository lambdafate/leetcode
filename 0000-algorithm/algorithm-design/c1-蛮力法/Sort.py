"""
    select-sort, bubble-sort
"""


def select_sort(array):
    for i in range(0, len(array)-1):
        tmp = i
        for j in range(i+1, len(array)):
            if array[tmp] > array[j]:
                tmp = j
        array[i], array[tmp] = array[tmp], array[i]
    return array


def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 3, 10, 2]
    print(f"array: {array}")
    print(f"select sort => {select_sort(array)}")
    print(f"bubble sort => {bubble_sort(array)}")