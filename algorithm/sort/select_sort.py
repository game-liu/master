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


def select_sort_1(l: List) -> List:
    if not l:
        return []
    ret = []
    for i in range(len(l)):
        min_data = min(l)
        ret.append(min_data)
        l.remove(min_data)
    return ret


def select_sort_2(l: List) -> None:
    # 把每趟最小的值放在最前面，跟无序区第一个交换位置
    for i in range(len(l) - 1):  # 第i趟,最后一趟不用再进行排序，只有一个元素
        min_index = i
        for j in range(i + 1, len(l)):  # i前面已经是有序区，顾不需要再进行排序
            if l[min_index] < l[j]:
                min_index = j
        if min_index != i:
            l[i], l[min_index] = l[min_index], l[i]
        print(l)


if __name__ == "__main__":
    arr = [0, 1, 4, 2, 6, 3, 8, 7, 9]
    # ret = select_sort(arr)
    # ret = select_sort_1(arr)
    # print(ret)
    select_sort_2(arr)
