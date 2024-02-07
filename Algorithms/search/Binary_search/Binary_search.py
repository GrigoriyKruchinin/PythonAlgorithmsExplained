def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 6
result = binary_search(my_list, target_value)
if result != -1:
    print(f"Элемент {target_value} найден по индексу {result}.")
else:
    print(f"Элемент {target_value} не найден в списке.")
