#                                    Задача 4
# Поиск последнего вхождения элемента в отсортированном списке: 
# У вас есть отсортированный список чисел и целевое значение. 
# Напишите функцию find_last_occurrence(arr, target), которая 
# использует бинарный поиск для поиска индекса последнего 
# вхождения целевого значения в списке. 
# Если целевое значение не найдено, вернуть -1.

def find_last_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            res = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return res


# Пример использования для задачи 4
sorted_list = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7, 8, 9, 10]
target_value = 4

result = find_last_occurrence(sorted_list, target_value)

if result != -1:
    print(f"Последнее вхождение {target_value} в списке находится по индексу: {result}")
else:
    print(f"{target_value} не найдено в списке.")
