from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        if node not in graph:
            continue
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I', 'J'],
    'F': [],
    'G': ['K'],
    'H': [],
    'I': [],
    'J': ['L'],
    'K': [],
    'L': []
}

print("Output of above graph:")
bfs(graph, 'A')
