# 直接插入排序
def insert_sort(lists):
    n = len(lists)
    for i in range(1, n):
        key = lists[i]
        j = i - 1
        while j >= 0 and lists[j] > key:
            lists[j + 1] = lists[j]
            lists[j] = key
            j -= 1
    return lists


# 希尔排序-插入排序
def shell_sort(lists):
    length = len(lists)
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            temp = lists[i]
            j = i
            a = lists[j - gap]
            while j >= gap and temp < lists[j - gap]:
                lists[j] = lists[j - gap]
                j -= gap
                lists[j] = temp
        gap //= 2
    return lists


if __name__ == "__main__":
    gap = [5, 3, 1]
    L = [45, 34, 78, 12, 34, 32, 64]
    ret = shell_sort(L)
    # ret = insert_sort(L)
    print(ret)
