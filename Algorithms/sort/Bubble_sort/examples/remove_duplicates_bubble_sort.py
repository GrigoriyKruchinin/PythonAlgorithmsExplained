#                                 Задача 3
# Напишите функцию find_kth_smallest(arr, k), которая принимает список
# целых чисел arr и число k. Функция должна возвращать k-е наименьшее
# число из списка. Используйте сортировку пузырьком для решения этой задачи.


def find_kth_smallest(arr, k):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[k - 1]


my_list = [12, 4, 7, 2, 9, 1, 18, 14]
k = 3
result = find_kth_smallest(my_list, k)
print(f"{k}-е наименьшее число: {result}")
