def binary_search(arr, target):
    low = 0
    height = len(arr) - 1
    while low <= height:
        mid = (low + height) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            height = mid - 1
        else:
            low = mid + 1
    return False


if __name__ == "__main__":
    arr = [1, 3, 4, 6, 7, 9, 10]
    target = 4
    res = binary_search(arr, target)
    print(res)
