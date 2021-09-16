def bubble_sort(nums):
    if not nums:
        return None
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == '__main__':
    nums = [2, 4, 1, 4, 6, 3, 8, 0, 6, 5]
    ret = bubble_sort(nums)
    print(ret)
