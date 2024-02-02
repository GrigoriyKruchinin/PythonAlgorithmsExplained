#                               Задача 2
# Напишите функцию find_majority_element(arr), которая принимает список 
# целых чисел arr и возвращает элемент, который встречается более чем n/2 раз, 
# где n - длина списка. Если такого элемента нет, верните None. 
# Используйте сортировку слиянием для решения этой задачи.

def find_majority_element(arr):
    if len(arr) <= 1:
        return arr[0] if arr else None

    mid = len(arr) // 2
    left_half = find_majority_element(arr[:mid])
    right_half = find_majority_element(arr[mid:])

    # Если оба подмассива возвращают одинаковый элемент, это и есть мажоритарный элемент
    if left_half == right_half:
        return left_half

    # Иначе, сравниваем количество вхождений в левом и правом подмассивах
    left_count = arr.count(left_half)
    right_count = arr.count(right_half)

    if left_count > len(arr) // 2:
        return left_half
    if right_count > len(arr) // 2:
        return right_half 
    else: 
        return None


arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
result = find_majority_element(arr)
print(result)