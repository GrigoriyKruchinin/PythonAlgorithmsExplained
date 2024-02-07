#                                      Задача 1
# Сортировка по убыванию с сохранением порядка повторяющихся элементов:
# Реализуйте функцию quick_sort_desc(arr), которая сортирует список в
# порядке убывания с использованием быстрой сортировки, при этом сохраняя
# порядок повторяющихся элементов.


def quick_sort_desc(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]

    return quick_sort_desc(left) + mid + quick_sort_desc(right)


my_list = [4, 2, 3, 1, 4, 2, 5]
result = quick_sort_desc(my_list)
print("Отсортированный массив:", result)
