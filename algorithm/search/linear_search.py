# 顺序查找，也叫线性查找，从第一个列表元素开始对往后查找，直到查找到想要元素或者元素查找完
from typing import List


def linear_search(l: List, val: int) -> int:
    for index, value in enumerate(l):
        if value == val:
            return index
    return -1


if __name__ == '__main__':
    l = [2, 4, 3, 5, 6, 7, 0, 8, 7, 9]
    v = 4
    ret = linear_search(l, v)
    print(ret)
