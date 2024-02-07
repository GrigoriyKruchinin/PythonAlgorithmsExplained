#                               Задача 2
# Поиск медианы в неотсортированном списке:
# Реализуйте функцию find_median_unsorted(arr), которая принимает неотсортированный
# список и использует быструю сортировку для нахождения медианы списка.
# Верните найденную медиану.
# Если длина списка четная то верните среднее между двумя медианными значениями.


def find_median_unsorted(arr):
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return quick_sort(left) + mid + quick_sort(right)

    sorted_arr = quick_sort(arr)
    n = len(sorted_arr)
    if n % 2 == 1:
        return sorted_arr[n // 2]
    else:
        mid1 = sorted_arr[(n // 2) - 1]
        mid2 = sorted_arr[n // 2]
        return (mid1 + mid2) / 2


my_list = [64, 25, 12, 22, 11, 13]
result = find_median_unsorted(my_list)
print("Медиана списка:", result)