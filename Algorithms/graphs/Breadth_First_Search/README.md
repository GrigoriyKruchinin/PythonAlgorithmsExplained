### Название (Name)
Обход в ширину (Breadth-First Search, BFS)

#### Описание (Description)
Обход в ширину (BFS) - это алгоритм обхода или поиска данных в графе, который начинает с указанной вершины и поочередно посещает все соседние вершины текущей, а затем переходит к следующей "уровню" соседних вершин.

#### Структура (Structure)
1. Выбираем начальную вершину и помещаем ее в очередь.
2. Помечаем начальную вершину как посещенную.
3. Пока очередь не пуста, выполняем следующее:
    a. Извлекаем вершину из очереди.
    b. Для каждой соседней вершины, которая еще не была посещена:
      - Помечаем ее как посещенную.
      - Помещаем ее в очередь.
4. Повторяем шаги 3, пока все вершины не будут посещены.

#### Реализация (Realization)
```
from collections import deque

def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)

    while queue:
        current_vertex = queue.popleft()
        print(current_vertex, end=" ")

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

#### Пример использования
```
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

bfs(my_graph, "A")
```

#### О-нотация (Big O Notation)
Сложность алгоритма обхода в ширину - O(V + E), где V - количество вершин, E - количество ребер в графе.

#### Задачи на прокачку (Tasks)
**Задача 1**
Поиск кратчайшего пути в невзвешенном графе:
Реализуйте функцию shortest_path(graph, start_vertex, end_vertex), которая находит кратчайший путь между start_vertex и end_vertex в невзвешенном графе. Верните список вершин, составляющих кратчайший путь, или пустой список, если путь не существует.

**Задача 2**
Определение наличия цикла в графе:
Реализуйте функцию has_cycle(graph), которая определяет, содержит ли граф циклы. Верните True, если граф содержит циклы, и False в противном случае.