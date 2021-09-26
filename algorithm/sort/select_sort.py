from typing import List


def search_min(arr: List) -> int:
    min_data = arr[0]
    min_index = 0
    for i in range(len(arr)):
        if arr[i] < min_data:
            min_data = arr[i]
            min_index = i
    return min_index


def select_sort(arr: List) -> List:
    result = []
    for i in range(len(arr)):
        ret = search_min(arr)
        result.append(arr.pop(ret))
    return result


if __name__ == "__main__":
    arr = [0, 1, 4, 2, 6, 3, 8, 7, 9]
    ret = select_sort(arr)
    print(ret)
