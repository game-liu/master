from typing import List


def partition(a: List, left: int, right: int) -> int:
    pivot = a[left]  # 基值
    while left != right:  # 保证左右不等
        while left < right and a[right] > pivot:  # 从右边找一个比基值小的数
            right -= 1  # 未曾找到，左移一步
        a[left] = a[right]  # 如果找到，左边空位（基值的位置）存放找到的值，如果都比基值大，即left==right，存放他自己
        while left < right and a[left] <= pivot:  # 从左边找一个小于等于基值的数
            left += 1  # 未曾找到，则右移一步
        a[right] = a[left]  # 如果找到，则右边空位存放该数
    a[left] = pivot  # 此时left==right 将基值放到找到的位置中
    return left  # 返回此时基值的位置


def quick_sort(a, l, r):
    if not a or l >= r:
        return
    pivoits = [(l, r)]
    while len(pivoits) > 0:
        pivoit = pivoits.pop(0)
        piviot_num = partition(a, l, r)
        if piviot_num - 1 > pivoit[0]:
            pivoits.append((pivoit[0], piviot_num - 1))
        if piviot_num + 1 <= pivoit[1]:
            pivoits.append((piviot_num + 1, pivoit[1]))


if __name__ == "__main__":
    a = [2, 4, 1, 55, 33, 6, 2, 0, 8, 5]
    l, r = 0, len(a) - 1
    quick_sort(a, l, r)
    print(a)
