#                                    Задача 1
# Напишите функцию find_minimum(arr), которая принимает список arr
# и возвращает минимальный элемент. Используйте сортировку пузырьком
# для решения этой задачи.


def find_minimum(arr):
    l = len(arr)
    for i in range(l):
        for j in range(l - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[0]


my_list = [4, 2, 8, 1, 9, 6]
result = find_minimum(my_list)
print(f"Минимальный элемент в списке: {result}")
