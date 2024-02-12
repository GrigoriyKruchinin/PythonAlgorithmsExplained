import heapq


def dijkstra(graph, start_vertex):
    # Инициализация расстояний: все вершины находятся на бесконечном расстоянии от начальной вершины
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start_vertex] = 0

    # Приоритетная очередь для хранения пар (расстояние, вершина)
    priority_queue = [(0, start_vertex)]

    # Основной цикл алгоритма Дейкстры
    while priority_queue:
        # Извлечение вершины с наименьшим расстоянием
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропуск вершины, если ее текущее расстояние больше, чем извлеченное
        if current_distance > distances[current_vertex]:
            continue

        # Обновление расстояний для соседей текущей вершины
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если найден более короткий путь к соседу, обновляем расстояние и добавляем в очередь
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Пример взвешенного графа
my_weighted_graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "D": 2, "E": 7},
    "C": {"A": 4, "F": 5, "G": 2},
    "D": {"B": 2},
    "E": {"B": 7, "H": 1},
    "F": {"C": 5},
    "G": {"C": 2},
    "H": {"E": 1},
}


start_vertex = "A"
result = dijkstra(my_weighted_graph, start_vertex)
print(f"Кратчайшие расстояния от вершины {start_vertex}: {result}")
