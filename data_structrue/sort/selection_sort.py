def selection_sort(nums):
    if not nums:  # 如果数组为空，直接返回None
        return None
    n = len(nums)
    for i in range(n):  # 遍历数组，遭到最小值
        min_index = i  # 假设当前下标为最小值的小标
        for j in range(i, n):  # 从当前下标开始往后遍历数组，当前下标之前的数组已经排序完成
            if nums[j] < nums[min_index]:  # 倘若下标j的值比假设最小下标值还要小，记录最小值的下标，重复该过程，找到最小值
                min_index = j  # 记录较小值的下标
        nums[i], nums[min_index] = nums[min_index], nums[i]  # 将最小值和假设最小值交换位置
    return nums  # 排序完成，返回排序后的数组


if __name__ == '__main__':
    nums = [2, 1, 3, 6, 4, 3, 7, 8, 9, 5, 4]
    ret = selection_sort(nums)
    print(ret)
