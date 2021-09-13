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


def quick_sort(a, l, r):
    if not a or l >= r:
        return
    pivot_id = partition(a, l, r)  # 找到基值位置
    quick_sort(a, l, pivot_id - 1)  # 对基值左边的再排序
    quick_sort(a, pivot_id + 1, r)  # 对基值右边的再排序


if __name__ == '__main__':
    a = [2, 332, 4, 5, 65, 4, 5, 2]
    l = 0
    r = len(a) - 1
    quick_sort(a, l, r)
    print(a)
