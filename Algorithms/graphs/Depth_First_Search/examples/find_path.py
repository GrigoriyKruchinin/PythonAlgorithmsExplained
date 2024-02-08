#                               Задача 3
# Поиск пути в графе:
# Реализуйте функцию find_path(graph, start_vertex, end_vertex),
# которая принимает граф в виде списка смежности, начальную и конечную вершины,
# и возвращает путь между ними.
# Если пути нет, верните пустой список.


def find_path(graph, start_vertex, end_vertex):
    visited = set()
    result = []
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        visited.add(vertex)
        result.append(vertex)
        if vertex == end_vertex:
            break
        stack.extend(x for x in graph[vertex] if x not in visited)
    return result if end_vertex in result else []


# Пример использования
my_graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["B", "H"],
    "F": ["C"],
    "G": ["C"],
    "H": ["E"],
}

start_vertex = "A"
end_vertex = "D"
path = find_path(my_graph, start_vertex, end_vertex)

print(f"Путь из вершины {start_vertex} в вершину {end_vertex}: {path}")
