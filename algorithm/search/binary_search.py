# 二分查找，也叫折半查找,查找的是已经排序好的列表
from typing import List


def binary_search_2(l: List, val: int) -> int:
    if not l:
        return -1
    left = 0
    right = len(l) - 1
    while left <= right:  # 候选区还有值，继续循环
        mid = left + (right - left) // 2  # 防止整形溢出
        if l[mid] == val:  # 找到目标，返回位置下标
            return mid
        elif l[mid] > val:  # 目标值在中间位置左边，丢弃右边元素，查找左边即可
            right = mid - 1  # 顾最右边的值就是中间值的左侧
        else:  # 目标值在中间位置右边，丢弃左边元素，查找右边
            left = mid + 1
    return -1


if __name__ == '__main__':
    l = [1, 2, 4, 6, 7, 8, 9, 10]
    v = 4
    ret_2 = binary_search_2(l, v)
    print(f'ret_2:{ret_2}')
