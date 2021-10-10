import random


# 直接插入排序
def insert_sort(lists):
    n = len(lists)
    for i in range(1, n):  # 从第二个元素开始排，默认第一个元素已经是排好的
        key = lists[i]  # 基数为当前元素
        j = i - 1  # 从后开始扫描该元素之前的元素序列
        while j >= 0 and lists[j] > key:  # 如果当前元素比基数大的话，调换位置
            lists[j + 1] = lists[j]
            lists[j] = key
            j -= 1
    return lists


def insert_sort_1(l: list) -> None:
    if not l:
        return
    for i in range(1, len(l)):  # 默认第一个牌已经排好序，从第二个牌开始进行插入排序
        temp = l[i]  # 当前需要排序的牌
        j = i - 1  # 已经排好序的牌的下标
        while j >= 0 and l[j] > temp:  # j>=0为了防止当前需要排序的牌比手里的牌都要小，手里的牌都要往右挪
            l[j + 1] = l[j]  # 往右挪
            j -= 1  # 当前牌的下标
        l[j + 1] = temp  # 插入找好的位置
        print(l)


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
    L = list(range(1, 10))
    random.shuffle(L)  # 打乱列表
    print(L)
    # ret = insert_sort(L)
    # print(ret)
    insert_sort_1(L)
    print(L)
