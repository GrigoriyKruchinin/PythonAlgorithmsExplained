#                           Задача 2:
# Напишите функцию count_occurrences(arr, target),
# которая принимает список arr и целевое значение target.
# Функция должна вернуть количество раз, которое целевое значение встречается в списке.


def count_occurrences(arr, target):
    acc = 0
    for i in range(len(arr)):
        if arr[i] == target:
            acc += 1
    return acc


# Пример использования:
my_list = [4, 2, 8, 1, 8, 6, 8]
target_value = 8
result = count_occurrences(my_list, target_value)
print(f"Элемент {target_value} встречается {result} раз.")
