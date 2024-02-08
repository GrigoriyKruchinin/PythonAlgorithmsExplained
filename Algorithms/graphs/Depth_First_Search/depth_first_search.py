def dfs(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    result = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            stack.extend(
                neighbor for neighbor in graph[vertex] if neighbor not in visited
            )

    return result


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

print(dfs(my_graph, "B"))
