#                          Задача 2
# Напишите функцию is_sorted(arr), которая принимает список arr 
# и возвращает True, если список отсортирован по возрастанию, и 
# False в противном случае. Используйте сортировку пузырьком для 
# проверки порядка элементов.

def is_sorted(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                return False
    return True

my_list = [4, 2, 8, 1, 9, 6]
sorted_list = sorted(my_list)

if is_sorted(my_list):
    print(f"Список {my_list} отсортирован")
else:
    print(f"Список {my_list} не отсортирован")

if is_sorted(sorted_list):
    print(f"Список {sorted_list} отсортирован")
else:
    print(f"Список {sorted_list} не отсортирован")