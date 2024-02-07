#                           Задача 1:
# Напишите функцию find_second_element_index(arr, target),
# которая принимает список arr и целевое значение target.
# Функция должна вернуть индекс второго вхождения целевого значения в список,
# или -1, если целевое значение не найдено или присутствует один раз.


def find_second_element_index(arr, target):
    element_count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            if element_count == 0:
                element_count += 1
            else:
                return i
    return -1


# Пример 1
my_list = [4, 2, 8, 1, 8, 6, 8, 2]
target_value = 8
result = find_second_element_index(my_list, target_value)
print(f"Индекс второго вхождения элемента {target_value} в списке: {result}")

# Пример 2
my_list = [1, 2, 3, 4, 7, 5, 6]
target_value = 7
result = find_second_element_index(my_list, target_value)
print(f"Индекс второго вхождения элемента {target_value} в списке: {result}")
