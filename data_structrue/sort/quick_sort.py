from typing import List


def partition(a, l, r):  # 定位跟基值交换的数
    i = l
    j = r
    pivot = a[l]  # 基值定位最做的数值
    while i != j:
        while i < j and a[j] > pivot:  # 从右找比基值小的数
            j -= 1  # 停住
        while i < j and a[i] <= pivot:  # 从左找到比基值大或等于的数
            i += 1  # 停住
        if i < j:  # 如果两个值不相等，交换
            a[i], a[j] = a[j], a[i]
    a[l], a[i] = a[i], a[l]  # 基值再与两数较小的交换位置
    return i  # 返回基值当前位置，交换后的


def partition_1(a: List, left: int, right: int) -> int:
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
    # pivot_id = partition(a, l, r)  # 找到基值位置
    pivot_id = partition_1(a, l, r)  # 找到基值位置
    quick_sort(a, l, pivot_id - 1)  # 对基值左边的再排序
    quick_sort(a, pivot_id + 1, r)  # 对基值右边的再排序


if __name__ == '__main__':
    a = [2, 332, 4, 5, 65, 4, 5, 2]
    l = 0
    r = len(a) - 1
    quick_sort(a, l, r)
    print(a)

    
    
'''
非递归版本 （区别仅为Qsort方法，使用栈来保存中间结果），python3 执行
'''

# def swap(lst, left, right):
#     lst[left], lst[right] = lst[right], lst[left]
#
#
# def paritition(lst, left, right):
#     key = lst[left]
#     while left < right:
#         if left < right and key <= lst[right]:
#             right = right - 1
#         lst[left], lst[right] = lst[right], lst[left]
#
#         if left < right and lst[left] <= key:
#             left = left + 1
#         lst[left], lst[right] = lst[right], lst[left]
#     print('left: {} right: {} lst: {}'.format(left, right, lst))
#     return left
#
#
# def Qsort(lst, left, right):
#     piviots = [(left, right)]
#     while len(piviots) > 0:
#         piviot = piviots.pop(0)
#         if piviot[0] < piviot[1]:
#             piviot_num = paritition(lst, piviot[0], piviot[1])
#
#             if piviot_num - 1 > piviot[0]:
#                 piviots.append((piviot[0], piviot_num-1))
#
#             if piviot_num + 1 < piviot[1]:
#                 piviots.append((piviot_num+1, piviot[1]))
#
#
# def Quicksort(lst):
#     Qsort(lst, 0, len(lst) - 1)
#
#
# if __name__ == "__main__":
#     ll = [1, 20, 3, 50, 40, 70, 23, 100, 23]
#     Quicksort(ll)
