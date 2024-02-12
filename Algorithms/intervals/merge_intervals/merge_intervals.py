def merge_intervals(intervals: list[list]) -> list[list]:
    # Проверка, если интервалов 1 или меньше, то возвращаем их как есть
    if len(intervals) <= 1:
        return intervals

    # Сортируем интервалы по начальным значениям
    intervals.sort(key=lambda x: x[0])

    # Добавляем первый интервал в результат
    res = [intervals[0]]

    # Начинаем обход со второго интервала, сравнивая его с последним
    for i in range(1, len(intervals)):
        curr_start, curr_end = intervals[i]
        prev_start, prev_end = res[-1]

        # Проверяем, пересекаются ли текущий и предыдущий интервалы
        if prev_end >= curr_start:
            # Если да, то объединяем их
            res[-1] = [min(curr_start, prev_start), max(prev_end, curr_end)]
        else:
            # Если нет, добавляем текущий интервал в результат
            res.append(intervals[i])

    return res


# Пример использования:
intervals = [[2, 6], [1, 3], [8, 10], [15, 18]]
result = merge_intervals(intervals)
print(result)
