#                                      Задача 1
# Реализуйте функцию insertion_sort_desc(arr), которая сортирует список
# в порядке убывания с использованием сортировки вставками.


def insertion_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Пример использования
my_list = [12, 11, 13, 5, 6]
insertion_sort_desc(my_list)
print("Отсортированный массив:", my_list)
