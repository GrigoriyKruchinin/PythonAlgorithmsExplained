#                                   Задача 3
#                        Поиск повторяющихся элементов: 
# У вас есть отсортированный список чисел, например, [1, 2, 2, 3, 4, 4, 4, 5], 
# и целевое значение, например, 4. 
# Напишите функцию find_all_indices(arr, target), которая использует бинарный поиск
# для поиска всех индексов, по которым целевое значение встречается в списке, 
# и возвращает отсортированный список этих индексов.Если целевое значение не найдено, вернуть пустой список

def find_all_indices(arr, target):
    result = []
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            # Если найдено совпадение, добавляем индекс в список
            result.append(mid)
            
            left_ptr, right_ptr = mid - 1, mid + 1
            # Проверяем левую половину на наличие дополнительных совпадений
            while left_ptr >= left and arr[left_ptr] == target:
                result.append(left_ptr)
                left_ptr -= 1
            
            # Проверяем правую половину на наличие дополнительных совпадений
            while right_ptr <= right and arr[right_ptr] == target:
                result.append(right_ptr)
                right_ptr += 1
            
            return sorted(result)  # Возвращаем список индексов в отсортированном порядке
        
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result  # Если целевое значение не найдено, вернуть пустой список

# Пример использования:
my_list = [1, 2, 2, 3, 4, 4, 4, 5]
target_value = 4
result = find_all_indices(my_list, target_value)
print(f"Индексы элемента {target_value} в списке: {result}")

        
