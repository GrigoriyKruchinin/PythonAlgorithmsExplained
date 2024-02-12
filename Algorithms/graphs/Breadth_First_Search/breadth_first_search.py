from collections import deque


def bfs(graph, start_vertex):
    visited = set()
    visited.add(start_vertex)
    queue = deque([start_vertex])
    result = []

    while queue:
        current_vertex = queue.popleft()
        result.append(current_vertex)

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


#### Пример использования
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

print(bfs(my_graph, "B"))
