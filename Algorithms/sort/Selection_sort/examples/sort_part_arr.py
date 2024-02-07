#                                      Задача 1
# Сортировка частей массива: У вас есть массив чисел и два индекса.
# Напишите функцию sort_part_arr(arr, i, j), которая сортирует только часть
# массива между индексами start и end с использованием сортировки выбором.


def sort_part_arr(arr, start, end):
    if start < 0 or end > len(arr) or start >= end:
        print("Некорректные значения start и end")
        return arr

    part_to_sort = arr[start:end]

    n = len(part_to_sort)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if part_to_sort[j] < part_to_sort[min_index]:
                min_index = j
        part_to_sort[i], part_to_sort[min_index] = (
            part_to_sort[min_index],
            part_to_sort[i],
        )

    arr[start:end] = part_to_sort
    return arr


# Пример использования
my_list = [4, 2, 7, 1, 9, 5, 6]
sorted_list = sort_part_arr(my_list, 2, 5)
print(sorted_list)
