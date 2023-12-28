#                           Задача 1: 
# Напишите функцию count_inversions(arr), которая принимает список целых
# чисел arr и возвращает количество инверсий в списке. Инверсия - это пара 
# индексов (i, j), таких что i < j и arr[i] > arr[j]. 
# Используйте сортировку слиянием для решения этой задачи.

def count_inversions(arr):
    def merge(left, right):
        merged_list = []
        i = j = 0
        inv_count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged_list.append(left[i])
                i += 1
            else:
                merged_list.append(right[j])
                inv_count += len(left) - i
                j += 1

        merged_list.extend(left[i:])
        merged_list.extend(right[j:])

        return merged_list, inv_count

    def merge_sort_and_inv_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_sorted, inv_left = merge_sort_and_inv_count(left_half)
        right_sorted, inv_right = merge_sort_and_inv_count(right_half)

        merged, inv_merge = merge(left_sorted, right_sorted)

        return merged, inv_merge + inv_left + inv_right

    _, result = merge_sort_and_inv_count(arr)
    return result


my_list = [7, 2, 4, 1, 6, 3, 5]
result = count_inversions(my_list)
print(f"Количество инверсий: {result}")
