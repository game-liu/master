import random
from typing import List


def sift(li: List, low: int, height: int) -> None:
    """
    调整函数
    :param li:
    :param low:  堆的根节点位置
    :param height: 堆的最后一个元素的位置
    :return:
    """
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j开始是跟的左节点
    temp = li[low]  # 将根节点保存
    while j <= height:  # 保证不溢出
        if j + 1 <= height and li[j + 1] > li[j]:  # 在不溢出且左节点大于有节点
            j += 1  # j指向i的右孩子
        if li[j] > temp:
            li[i] = li[j]
            i = j  # 往下走一层
            j = 2 * i + 1
        else:
            # li[i] = temp
            break
    li[i] = temp  # 考虑i已经是最后一层，j是最后一层的下一层


def heap_sort(li: List) -> None:
    n = len(li)
    # leaf = (n-1)-1=n-2 最后一个叶子节点是长度减一
    for i in range((n - 2) // 2, -1, -1):
        # i代表建堆的时候调整部分的根
        sift(li, i, n - 1)
    # 至此，堆建好
    print(f"end li: {li}")
    for j in range(n - 1, -1, -1):
        # 开始排序
        # j指向当前堆最后一个元素
        li[0], li[j] = li[j], li[0]
        sift(li, 0, j - 1)
    print(f"finaly li:{li}")


if __name__ == "__main__":
    li = [i for i in range(10)]
    random.shuffle(li)
    print(f"sta li: {li}")
    heap_sort(li)
