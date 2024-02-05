def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Пример использования:
my_list = [4, 2, 8, 1, 9, 6]
target_value = 8
result = linear_search(my_list, target_value)
if result != -1:
    print(f"Элемент {target_value} найден по индексу {result}.")
else:
    print(f"Элемент {target_value} не найден в списке.")
