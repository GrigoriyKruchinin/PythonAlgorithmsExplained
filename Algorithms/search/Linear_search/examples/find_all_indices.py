#                 Задача 3:
# Задача: Напишите функцию find_all_indices(arr, target),
# которая принимает список arr и целевое значение target.
# Функция должна вернуть список индексов,
# по которым целевое значение встречается в списке.
# Если целевое значение не найдено, вернуть пустой список.


def find_all_indices(arr, target):
    indeces = []
    for i in range(len(arr)):
        if arr[i] == target:
            indeces.append(i)
    return indeces


# Пример использования:
my_list = [4, 2, 8, 1, 8, 6, 8, 2]
target_value = 8
result = find_all_indices(my_list, target_value)
print(f"Индексы элемента {target_value} в списке: {result}")
