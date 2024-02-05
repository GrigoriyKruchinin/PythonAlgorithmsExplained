#                                   Задача 2
#                   Поиск вращения в отсортированном списке:
# У вас есть отсортированный список чисел, который был вращен
# (например, [6, 1, 2, 3, 4, 5]).
# Напишите функцию find_rotation_index, которая использует бинарный поиск для поиска индекса,
# с которого начинается вращение списка (место, где произошел сдвиг),
# или возвращает -1, если список не был вращен.


def find_rotation_index(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Если левой границей меньше правой, значит список не вращался, возвращаем -1
        if arr[left] <= arr[right]:
            return -1

        mid = (left + right) // 2

        # Если средний элемент больше элемента справа от него, то это место вращения
        if arr[mid] > arr[mid + 1]:
            return mid + 1

        # Если средний элемент меньше элемента слева от него, то это место вращения
        if arr[mid] < arr[mid - 1]:
            return mid

        # Если текущий сегмент слева в "нормальном" порядке, идем в правую часть
        if arr[left] <= arr[mid]:
            left = mid + 1
        # Иначе, идем в левую часть
        else:
            right = mid - 1

    return -1  # Если список не вращался, возвращаем -1


# Пример использования:
my_list = [6, 1, 2, 3, 4, 5]
result = find_rotation_index(my_list)
if result != -1:
    print(f"Список был вращен, начало вращения по индексу {result}.")
else:
    print("Список не был вращен.")
