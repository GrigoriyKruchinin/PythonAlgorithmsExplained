#                               Задача 3
# Напишите функцию sort_dates(dates), которая принимает список дат в формате
# "YYYY-MM-DD" и возвращает список дат, отсортированный в порядке возрастания.
# Используйте сортировку слиянием для решения этой задачи.


def sort_dates(dates):
    def merge_sort(dates):
        if len(dates) <= 1:
            return dates
        mid = len(dates) // 2
        left = sort_dates(dates[:mid])
        right = sort_dates(dates[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    return merge_sort(dates)


dates = ["2023-01-15", "2022-02-10", "2022-01-25", "2022-01-05"]
sorted_dates = sort_dates(dates)
print(sorted_dates)
