#                                   Задача 1
#                   Поиск элемента в отсортированном списке:
# У вас есть отсортированный список чисел, например, [1, 3, 5, 7, 9, 11, 13, 15],
# и целевое значение, например, 7. Напишите функцию binary_search(arr, target),
# которая использует бинарный поиск для поиска целевого значения в списке и возвращает
# его индекс, если оно присутствует, или -1, если не найдено.


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Пример
my_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9
result = binary_search(my_list, target)
if result != -1:
    print(f"Элемент {target} найден по индексу {result}.")
else:
    print(f"Элемент {target} не найден в списке.")
