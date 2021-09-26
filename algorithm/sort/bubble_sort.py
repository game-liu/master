# 冒泡排序
import random
from typing import List


def bubble_sort(L: List) -> None:
    if not L:
        return None
    for i in range(len(L) - 1):  # 比较的第i趟
        flag = False
        for j in range(len(L) - i - 1):  # 比较完第几趟，就有几个元素不用再排序
            # 升序
            if L[j] > L[j + 1]:
                # 降序
                # if L[j] > L[j+1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                flag = True
        if not flag:
            return


if __name__ == '__main__':
    L = [random.randint(0, 1000) for _ in range(10)]
    print(f'start:{L}')
    bubble_sort(L)
    print(f'end:{L}')
