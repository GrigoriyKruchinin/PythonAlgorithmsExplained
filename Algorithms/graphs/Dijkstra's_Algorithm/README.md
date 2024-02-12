### Название (Name)
Алгоритм Дейкстры (Dijkstra's Algorithm)

#### Описание (Description)
Алгоритм Дейкстры используется для нахождения кратчайших путей от одной начальной вершины ко всем остальным вершинам во взвешенном графе.

#### Структура (Structure)
1. Инициализируем расстояния от начальной вершины до всех остальных вершин бесконечностью и расстояние от начальной вершины до самой себя нулем.
2. Создаем приоритетную очередь, где вершины отсортированы по их текущим расстояниям от начальной вершины.
3. Начинаем с начальной вершины и обновляем расстояния до соседних вершин, если новый путь короче.
4. Переходим к вершине с наименьшим текущим расстоянием и повторяем шаг 3, пока не посетим все вершины.

#### Реализация (Realization)
```
import heapq

def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0

    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
```

#### Пример использования
```
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
```

#### О-нотация (Big O Notation)
Сложность алгоритма Дейкстры - O((V + E) log V), где V - количество вершин, E - количество ребер во взвешенном графе.

#### Задачи на прокачку (Tasks)
**Задача 1**
Нахождение кратчайшего пути в ориентированном графе:
Реализуйте функцию shortest_path_directed(graph, start_vertex, end_vertex), которая находит кратчайший путь от start_vertex к end_vertex в ориентированном взвешенном графе. Верните список вершин, составляющих кратчайший путь, или пустой список, если путь не существует.

**Задача 2**
Поиск кратчайшего пути между всеми парами вершин:
Реализуйте функцию all_pairs_shortest_path(graph), которая находит кратчайшие пути между всеми парами вершин в ориентированном взвешенном графе. Верните матрицу расстояний, где элемент [i][j] представляет кратчайшее расстояние от вершины i к вершин