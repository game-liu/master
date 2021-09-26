def quick_sort(array):
    if len(array) < 2:
        return array
    base_data = array[0]
    left_array = [left_data for left_data in array[1:] if left_data <= base_data]
    right_array = [right_data for right_data in array[1:] if right_data > base_data]
    return quick_sort(left_array) + [base_data] + quick_sort(right_array)


if __name__ == "__main__":
    array = [3, 2, 5, 8, 0, 3, 6, 9, 1]
    ret = quick_sort(array)
    print(ret)


