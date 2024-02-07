#                                   Задача 3
# Сортировка строки без учета регистра:
# Реализуйте функцию quick_sort_case_insensitive(s), которая сортирует символы
# в строке в лексикографическом порядке без учета регистра.
# Например, для строки "AbraKadaBra" результатом должно быть "AaaaabBdKrr".


def quick_sort_case_insensitive(s):
    if len(s) <= 1:
        return s
    pivot = s[len(s) // 2]
    l = "".join(filter(lambda x: x.lower() < pivot.lower(), s))
    m = "".join(filter(lambda x: x.lower() == pivot.lower(), s))
    r = "".join(filter(lambda x: x.lower() > pivot.lower(), s))
    return quick_sort_case_insensitive(l) + m + quick_sort_case_insensitive(r)


string = "AbraKadaBra"
print(quick_sort_case_insensitive(string))
